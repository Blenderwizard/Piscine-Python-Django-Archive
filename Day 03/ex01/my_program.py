import local_lib.path as path

def my_function() -> None:
	path.Path("./temp").mkdir_p()
	path.Path("./temp/file").write_bytes(b'this is a file\n', append=True)
	print(path.Path("./temp/file").read_text('ascii'), end='')

if __name__ == '__main__':
	my_function()