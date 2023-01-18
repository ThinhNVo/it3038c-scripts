#!/bin/bash

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
TESTING=$(echo $DATA | jq '.[0].pending')
DEATH=$(echo $DATA | jq '.[0].death')
death=$(echo $DATA | jq '.[0].deathIncrease')
TODAY=$(date)

echo "On $TODAY, there are $POSITIVE positive COVID cases. Lucky for us, we also received $NEGATIVE negative
 COVID cases with $TESTING of undecided cases. Our casualty are $DEATH cases in total of which the number of
 deatch cases has risen by $death cases "

