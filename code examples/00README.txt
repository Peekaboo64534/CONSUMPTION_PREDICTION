
Create a new conda environment called IdealDataInterface via

conda env create -f environment.yml

source activate IdealDataInterface

You will need to add the API directory to your Python path (or copy
contents to your execute directory). For example:
 export PYTHONPATH=$PYTHONPATH:../API/

Now try running an example program or notebook. For example:

python roomdata_example.py --homeid 62 --measure humidity --inputdir /path/to/sensordata --samplerate 1000

