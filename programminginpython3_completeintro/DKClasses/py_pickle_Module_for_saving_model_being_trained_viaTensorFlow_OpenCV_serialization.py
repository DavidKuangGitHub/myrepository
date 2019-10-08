#py_pickle_Module_for_saving_model_being_trained_viaTensorFlow_OpenCV_serialization.py 
import pickle

example_dict = {1: "David", 2:"Kuang", 3:"Ford PD Engineer"}
print("Here Dictionary example_dict is  %s" %example_dict)

pickle_out  = open("model_trainedTwo.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

pickle_in = open("model_trainedTwo.pickle","rb")
example_dictDeSerialization = pickle.load(pickle_in)

print("DeSerialization Results are      %s" %example_dictDeSerialization)
