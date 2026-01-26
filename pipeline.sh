#!/usr/bin/env bash

set -e

WEBHOOK_URL="http://localhost:5678/webhook-test/a78c2256-c123-4280-b22d-b375ff664f36"
SESSION_ID="039347c069b54c99a9a3a0506107e088"
CONTENT_TYPE="Content-Type: application/json"

echo "🚀 STEP 1 — Documentation generation"
curl -s -X POST "$WEBHOOK_URL" \
  -H "$CONTENT_TYPE" \
  -d "{
    \"sessionId\": \"$SESSION_ID\",
    \"step\": 1,
    \"prompt\": \"Use only the generate_documentation tool to perform the step mentionned, STEP 1: Documentation generation.\",
    \"data\": {
      \"lore\": \"LLM Studio can make your life easier by doing everything you need for you web3 project\",
      \"hasMascot\": false,
      \"tone\": \"Serious\",
      \"taglineStyle\": \"Short & punchy\",
      \"projectType\": \"tool\",
      \"goal\": \"utility\",
      \"visualVibe\": \"clean\",
      \"palettes\": [\"indigo\", \"lime\"],
      \"outputs\": {
        \"logo\": true,
        \"banner\": false,
        \"pfp\": false,
        \"announcements\": false,
        \"memes\": false,
        \"stickers\": false,
        \"documentation\": true,
        \"onepager\": false,
        \"roadmap\": false,
        \"faq\": false
      }
    }
  }"

echo -e "\n✅ STEP 1 done\n"

sleep 5

echo "🌐 STEP 2 — Website static generation"
curl -s -X POST "$WEBHOOK_URL" \
  -H "$CONTENT_TYPE" \
  -d "{
    \"sessionId\": \"$SESSION_ID\",
    \"step\": 2,
    \"prompt\": \"Use only generate_landing_page tool to perform the step mentionned, STEP 2: Website static generation.\",
    \"data\": {
      \"lore\": \"LLM Studio can make your life easier by doing everything you need for you web3 project\",
      \"hasMascot\": false,
      \"tone\": \"Serious\",
      \"taglineStyle\": \"Short & punchy\",
      \"projectType\": \"tool\",
      \"goal\": \"utility\",
      \"visualVibe\": \"clean\",
      \"palettes\": [\"indigo\", \"lime\"],
      \"outputs\": {
        \"logo\": true,
        \"banner\": false,
        \"pfp\": false,
        \"announcements\": false,
        \"memes\": false,
        \"stickers\": false,
        \"documentation\": true,
        \"onepager\": false,
        \"roadmap\": false,
        \"faq\": false
      }
    }
  }"

echo -e "\n✅ STEP 2 done\n"

sleep 5

echo "🎨 STEP 3 — Multi-assets generation"
curl -s -X POST "$WEBHOOK_URL" \
  -H "$CONTENT_TYPE" \
  -d "{
    \"sessionId\": \"$SESSION_ID\",
    \"step\": 3,
    \"prompt\": \"Use only generate_visuals tool to perform the step mentionned, STEP 3: Multi-assets generation.\",
    \"data\": {
      \"lore\": \"LLM Studio can make your life easier by doing everything you need for you web3 project\",
      \"hasMascot\": false,
      \"tone\": \"Serious\",
      \"taglineStyle\": \"Short & punchy\",
      \"projectType\": \"tool\",
      \"goal\": \"utility\",
      \"visualVibe\": \"clean\",
      \"palettes\": [\"indigo\", \"lime\"],
      \"outputs\": {
        \"logo\": true,
        \"banner\": false,
        \"pfp\": false,
        \"announcements\": false,
        \"memes\": false,
        \"stickers\": false,
        \"documentation\": true,
        \"onepager\": false,
        \"roadmap\": false,
        \"faq\": false
      }
    }
  }"

echo -e "\n🎉 PIPELINE COMPLETED SUCCESSFULLY"
