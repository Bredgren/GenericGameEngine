
TEST_DIR = "test"
TEST_SPEC = "TestSpec.txt"

def handleTest(test_name):
    print "Running test {}".format(test_name)
    exec("from {}.{} import runTest".format(TEST_DIR, test_name))
    runTest()
    print "{}: PASS\n".format(test_name)

def main():
    f = open(TEST_SPEC)
    for test_name in f:
        handleTest(test_name.strip())
    f.close()

if __name__ == "__main__":
    main()
