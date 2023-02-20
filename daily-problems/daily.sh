#! /bin/sh
function getDaily() {
        curl --request POST \
          --url https://leetcode.com/graphql \
          --header 'Content-Type: application/json' \
          --data '{"query":"query questionOfToday{activeDailyCodingChallengeQuestion{link}}",
          "operationName":"questionOfToday"}'
}

firefox $(getDaily | \python3 -c "import sys, json; print('https://leetcode.com' + json.load(sys.stdin)['data']['activeDailyCodingChallengeQuestion']['link'])")  https://practice.geeksforgeeks.org/problem-of-the-day https://www.codingninjas.com/codestudio/problem-of-the-day
