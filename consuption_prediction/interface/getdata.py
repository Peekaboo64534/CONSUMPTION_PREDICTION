import pandas as pd

# Function to load CSV data into a DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to transform datetime columns
def transform_datetime_columns(df):
    df['starttime'] = pd.to_datetime(df['starttime'], format='%d/%m/%Y %H:%M')
    df['start_date'] = pd.to_datetime(df['starttime'].dt.date)
    df['start_time'] = df['starttime'].dt.time
    df['endtime'] = pd.to_datetime(df['endtime'], format='%d/%m/%Y %H:%M')
    df['end_date'] = df['endtime'].dt.date
    df['end_time'] = df['endtime'].dt.time
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    return df

# Function to replace floor values and map income bands
def replace_floor_and_map_income(df, floor_mapping):
    df['entry_floor'] = df['entry_floor'].replace(floor_mapping)
    unique_income_bands = df['income_band'].unique()
    income_band_mapping = {band: i for i, band in enumerate(unique_income_bands)}
    df['income_band_num'] = df['income_band'].map(income_band_mapping)
    return df

# Main function to load and process all data
def main():
    csv_paths = {
        'home': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/home.csv",
        'appliance': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/appliance.csv",
        'location': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/location.csv",
        'meterreading': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/meterreading.csv",
        'other_appliance': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/other_appliance.csv",
        'person': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/person.csv",
        'room': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/room.csv",
        'sensor': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/sensor.csv",
        'sensorbox': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/sensorbox.csv",
        'tariff': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/tariff.csv",
        'weatherfeed': "/mnt/c/Users/Usuario/OneDrive/Projeto energypricing/metadata_and_surveys/metadata/weatherfeed.csv",
    }

    # Load data into DataFrames
    df_home = load_data(csv_paths['home'])
    df_appliance = load_data(csv_paths['appliance'])
    df_location = load_data(csv_paths['location'])
    df_reading = load_data(csv_paths['meterreading'])
    df_oth_app = load_data(csv_paths['other_appliance'])
    df_person = load_data(csv_paths['person'])
    df_room = load_data(csv_paths['room'])
    df_sensor = load_data(csv_paths['sensor'])
    df_sensorbox = load_data(csv_paths['sensorbox'])
    df_tariff = load_data(csv_paths['tariff'])
    df_weatherfeed = load_data(csv_paths['weatherfeed'])

    # Process home DataFrame
    df_home = transform_datetime_columns(df_home)

    # Define floor mapping dictionary
    floor_mapping = {
        'Basement (level -1)': -1,
        'Ground': 0,
        '1st': 1,
        '2nd': 2,
        '3rd': 3,
        '4th': 4,
        '5th': 5,
        'Attic': 6
    }

    # Apply floor and income band transformations
    df_home = replace_floor_and_map_income(df_home, floor_mapping)

    # Calculate days between start_date and end_date
    df_home['days_between'] = (df_home['end_date'] - df_home['start_date']).dt.days

    # Drop unnecessary columns from home DataFrame
    columns_to_drop = [
        'install_type', 'starttime', 'starttime_enhanced', 'endtime', 'cohortid',
        'smart_automation', 'income_band', 'study_class', 'outdoor_drying',
        'outdoor_space', 'occupancy', 'urban_rural_name', 'build_era',
        'new_build_year', 'smart_monitors', 'start_time', 'end_time', 'urban_rural_class'
    ]
    df_home = df_home.drop(columns=columns_to_drop)

    # Process appliance DataFrame
    appliance_counts = df_appliance.groupby(['homeid', 'powertype'])['appliancetype'].nunique().reset_index()
    df_appliance_proc = appliance_counts.pivot(index='homeid', columns='powertype', values='appliancetype').fillna(0)
    df_appliance_proc = df_appliance_proc.rename(columns={'electric': 'electric_appliance', 'gas': 'gas_appliance'})
    df_appliance_proc = df_appliance_proc.reset_index()
    df_appliance_proc['electric_appliance'] = df_appliance_proc['electric_appliance'].astype(int)
    df_appliance_proc['gas_appliance'] = df_appliance_proc['gas_appliance'].astype(int)
    selected_columns = ['homeid', 'electric_appliance', 'gas_appliance']
    df_appliance_proc = df_appliance_proc[selected_columns]

    # Process person DataFrame
    selected_columns = ['homeid', 'primaryparticipant', 'ageband', 'workingstatus']
    df_person = df_person[selected_columns]

    # Process room DataFrame
    df_room1 = df_room.groupby('homeid')['floorarea'].sum().reset_index()
    df_room1 = df_room1.rename(columns={'floorarea': 'total_area'})

    df_room_proc = df_room.groupby('homeid')['type'].count().reset_index()
    df_room_proc = df_room_proc.rename(columns={'type': 'room_count'})

    df_room_proc_merge = pd.merge(df_room1, df_room_proc, on='homeid', how='left')

    df_room_proc1 = df_room.groupby('homeid')['windowsopen'].sum().reset_index()
    df_room_proc1 = df_room_proc1.rename(columns={'windowsopen': 'windows_open'})

    df_room_merge = pd.merge(df_room_proc_merge, df_room_proc1, on='homeid', how='left')

    # Process sensor DataFrame
    selected_columns = ['sensorboxid', 'roomid', 'type']
    df_sensor = df_sensor[selected_columns]

    # Process sensorbox DataFrame
    selected_columns = ['sensorboxid', 'sensorbox_type', 'heightfromfloor']
    df_sensorbox = df_sensorbox[selected_columns]

    # Process weatherfeed DataFrame
    selected_columns = ['feedid', 'weather_type', 'locationid']
    df_weatherfeed = df_weatherfeed[selected_columns]

    # Merge processed DataFrames
    merged_df = pd.merge(df_home, df_appliance_proc, on='homeid', how='left')
    merged_df = pd.merge(merged_df, df_room_merge, on='homeid', how='left')

    merged_df.to_csv('masterfeatures.csv', index=False)

    return None



if __name__ == "__main__":
    main()
