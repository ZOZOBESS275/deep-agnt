# Build a model client

The wrapper every team writes around a model API, as 27 small functions: hold a conversation, finish a cut-off reply, get JSON that validates, read a stream, retry a busy API and count what it cost.

Built step by step on [Deep-Agnt](https://deep-agnt.com/projects/model-client): 12 of 27 steps passed, each graded by tests.

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
