import collections


FunctionCom = collections.namedtuple(
    "FunctionCom", ['func', 'provider', 'url'])

FunctionMath = collections.namedtuple(
    "FunctionMath", ['func', 'provider', 'url'])

FunctionML = collections.namedtuple(
    "FunctionML", ['func', 'provider', 'url'])

FunctionLocal = collections.namedtuple(
    "FunctionLocal", ['func', 'provider', 'url'])


functionsMath = [
    FunctionMath(func="math", provider="aws",
                 url="https://4gyhrx3mv5.execute-api.us-east-1.amazonaws.com/dev/fft"),
    FunctionMath(func="math", provider="az",
                 url="https://thesisbenchmark.azurewebsites.net/api/fft"),
    FunctionMath(func="math", provider="goo",
                 url="https://us-central1-tesis-gcl.cloudfunctions.net/math"),
    FunctionMath(func="math", provider="ibm",
                 url="https://us-south.functions.cloud.ibm.com/api/v1/web/jpmartinez1%40utpl.edu.ec_dev/default/math-dev-fft.json"),
]

functionsCom = [
    FunctionCom(func="com", provider="aws",
                url="https://4gyhrx3mv5.execute-api.us-east-1.amazonaws.com/dev/com"),
    FunctionCom(func="com", provider="az",
                url="https://thesisbenchmark.azurewebsites.net/api/fft"),
    FunctionCom(func="com", provider="goo",
                url="https://us-central1-tesis-gcl.cloudfunctions.net/main"),
    FunctionCom(func="com", provider="ibm",
                url="https://us-south.functions.cloud.ibm.com/api/v1/web/jpmartinez1%40utpl.edu.ec_dev/default/com-dev-com.json"),
]

functionsML = [
    FunctionML(func="ml", provider="aws",
               url="https://4gyhrx3mv5.execute-api.us-east-1.amazonaws.com/dev/ml"),
    FunctionML(func="ml", provider="az",
               url="https://thesisbenchmark.azurewebsites.net/api/ml"),
    FunctionML(func="ml", provider="goo",
               url="https://us-central1-tesis-gcl.cloudfunctions.net/ml")
]

functionsLocal = [
    FunctionLocal(func="math", provider="local",
                  url="http://localhost:7071/api/fft"),
    FunctionLocal(func="ml", provider="local",
                  url="http://localhost:7071/api/ml")
]
