import slash
@slash.parametrize(('fruit','color'),[('apple','red'),('apple','green'),('apple','yellow')])
def test_fruits(fruit,color):
	assert fruit == "apple"