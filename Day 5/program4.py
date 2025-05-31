#serialization (python object to byte stream) and deserialization (byte stream to python object) using pickle module
#serialization  (dump() and dumps())
import pickle
data={'name':'aasif','age':22,'gender':'male'}
with open('data.txt','wb') as f:
    pickle.dump(data,f)

with open('data.txt','rb') as f:
    new_data=pickle.load(f)
print(new_data,type(new_data))