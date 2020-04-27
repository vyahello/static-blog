#!/bin/bash


run-pylint-analysis() {
    echo "Running pylint analysis ..." && ( pylint $(find "./" -iname "*.py") )
}


run-black-analysis() {
    echo "Running black analysis ..." && ( black --check "./" )
}


main() {
    run-pylint-analysis && run-black-analysis
    return 0
}


main
