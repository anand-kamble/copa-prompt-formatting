# AI Grader

This project aims to develop a completely automated grading system using a Large Language Model (LLM).

## Execution
To set up and run the project, follow these steps:

1. **Activate the Poetry shell:**
   ```bash
   poetry shell
   ```
2. **Install the dependencies:**
   ```bash
   poetry install
   ```
3. **Run the application:**
   ```bash
   ./run.sh
   ```

## Details

### Basic Flow of the Program

1. **Loading Answers:**
   - The answers are loaded from pickle files generated by Python scripts used for grading.
   
2. **Creating a Prompt:**
   - A prompt is created using the loaded answers. This prompt includes the correct answer, context, and the student's answer.
   
3. **Invoking the LLM:**
   - The LLM is invoked with all the provided information.
   - The `invoke_llm` function in the program is traced by LangSmith, recording all the runs which can be viewed on the LangSmith dashboard.

## Future Work
1. Improve the method for providing context to the LLM.
2. Format the output from the model for better readability and usability.

## Notes
The following packages were added to run the Mixtral model, but the output was not convincing enough to use it:
```toml
sentencepiece = "^0.2.0"
protobuf = "^5.27.0"
```

## Problems Faced

### Poetry Install Stuck at Pending State
The installation process was stuck at the pending state. The issue was resolved by running the following command:
```bash
export PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring
```
This solution was found by following the instructions mentioned in [this GitHub issue](https://github.com/python-poetry/poetry/issues/7235).

---