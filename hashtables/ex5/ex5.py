# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for item in queries:
        # add queries to cache
        cache[item] = [item]

    result = []

    for item in files:
        #check if last part of file path is in cache
        if item.split("/")[-1] in cache:
            result.append(item)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
