# Bowling API

___
## Development Server
```
./dev_srv.sh
```

___
## Tests, Linting, Code Coverage

The main testing script is `./run_tests.sh`.

It has further capabilities to give output on linting, code coverage reports, and a more verbose output.

<!-- - <strong style="color:red">The database will typically get dumped and rebuild with seeded data...</strong>
To prevent this, use the command `nodb` at the end of `./run_tests.sh`.  It is good to run the tests with a fresh DB, but it can slow down test development time if you are doing it each time.
**eg** => `./run_tests.sh nodb` -->

- In order to further speed up test development time, you can limit the output to be one or a set of modules:
**eg** => `./run_tests.sh auth users` will run the test suite for auth and users endpoints.

- Add the following to the end of `./run_tests.sh` to get further output:
`cov` => code coverage
`lint` => linting with flake8
`full` => more verbose output for tests

An example running all is: `./run_tests.sh cov lint full`

___
## Main Endpoint

Make a call to localhost:8080/api/bowl as a POST.
The payload should be similar to the following:
```
[
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10
]

Where the numbers are the quantity of pins knocked down in each throw.

The assumptions made for incoming data are:
- The input numbers are valid for a given a 10 frame bowling game
- "rolls" are valid I.E. there aren't 11 pins in a frame and no negative
- there will be the correct number of frames and rolls to fit a full game - no more, no less
- only the final score will be given
