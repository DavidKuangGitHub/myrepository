import slash
@slash.parametrize('x',[1,2,3,100])
def test_something(x):
	assert x<5
print("Python running is completed!")
