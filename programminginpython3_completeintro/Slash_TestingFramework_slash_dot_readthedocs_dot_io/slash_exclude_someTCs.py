import slash

SUPPORTED_SIZES=[10,15,20,25]

@slash.parametrize('size',SUPPORTED_SIZES)
@slash.exclude('size',[10,20])
def test_size(size):
	assert size not in [10,20]