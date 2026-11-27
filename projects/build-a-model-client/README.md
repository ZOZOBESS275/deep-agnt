# Build a model client

The wrapper every team writes around a model API, as 27 small functions: hold a conversation, finish a cut-off reply, get JSON that validates, read a stream, retry a busy API and count what it cost.

Built step by step on [Deep-Agnt](https://deep-agnt.com/projects/model-client): 26 of 27 steps passed, each graded by tests.

- [x] Step 1: A user message
- [x] Step 2: An assistant message
- [x] Step 3: Add a turn to the history
- [x] Step 4: The text of a reply
- [x] Step 5: Was the reply cut off?
- [x] Step 6: The tokens a reply used
- [x] Step 7: Make the call
- [x] Step 8: Get the rest of a cut-off reply
- [x] Step 9: Take off the code fence
- [x] Step 10: Find the JSON object
- [x] Step 11: Say what is wrong with it
- [x] Step 12: Write the correction
- [x] Step 13: Ask until the JSON is right
- [x] Step 14: The text in one event
- [x] Step 15: Join the stream
- [x] Step 16: Why the stream ended
- [x] Step 17: A reply from a stream
- [x] Step 18: Which errors are worth retrying
- [x] Step 19: How long to wait
- [x] Step 20: Retry with backoff
- [x] Step 21: Price one call
- [x] Step 22: Keep a ledger
- [x] Step 23: Print the receipt
- [x] Step 24: Start a client
- [x] Step 25: One call, retried and counted
- [x] Step 26: Send a message
