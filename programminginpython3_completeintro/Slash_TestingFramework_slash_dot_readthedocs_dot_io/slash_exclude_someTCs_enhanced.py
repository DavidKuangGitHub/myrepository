import slash

SUPPORTED_SIZES=[10,15,20,25]
@slash.exclude(('car.size','car.color'),[(10,'red'),(20,'blue')])
def test_ca(car):
	assert car not in [(10,'red'),(20,'blue')]

@slash.parametrize('size',SUPPORTED_SIZES)
@slash.parametrize('color',['red','green','blue'])
@slash.fixture
def car(size,color):
	return (size,color)