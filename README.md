# Bowling API

___
## Initial setup
Have python 3.8.5+ installed and active as base `python3` and pip must be installed for python 3 as `pip3` then run:  
```
./init.sh
```

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
**eg** => `./run_tests.sh bowl` will run the test suite for bowl endpoints.

- Add the following to the end of `./run_tests.sh` to get further output:  
`cov` => code coverage  
`lint` => linting with flake8  
`full` => more verbose output for tests  

An example running all is: `./run_tests.sh cov lint full`

**Generally** you would run `./run_tests.sh cov lint` for a full test including only important warnings/errors

___
## Main Endpoint

Make a call to localhost:8000/api/bowl as a POST.

An example CURL command is:
```
curl -X POST localhost:8000/api/bowl -H 'Content-Type: application/json' -d '[10,10,10,10,10,10,10,10,10,10,10,10]'
```

Where the numbers are the quantity of pins knocked down in each throw/bowl.

**The assumptions made for incoming data are:**
- The input numbers are **valid** for a given a 10-frame 10-pin bowling game
- "rolls" or "bowls" are valid I.E. there aren't 11 pins in a frame and no negative score
- there will be the correct number of frames and rolls to fit a full game - no more, no less
- only the final score will be given
