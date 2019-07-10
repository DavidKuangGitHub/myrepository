import slash
@slash.parameters.iterate(x=[1,2,3],y=[5,6,7])
def test_slash_parameters_dot_iterate(x,y):
	assert x+y<11