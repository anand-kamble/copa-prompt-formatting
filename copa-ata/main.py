# %%
import os
from typing import Any, List

from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline
from langsmith import traceable
from pandas import read_csv

load_dotenv()


def load_examples(filename:str, n:int = None) -> str:
    return read_csv(filename,nrows=n).to_string(index=False)

def load_ATA_info() -> str:
    file = open("ATA-info.txt", "r")
    info = file.readlines()
    file.close()
    return info
    
    
def format_prompt(
    fault: str, example: str = "No example provided",details:str = None
) -> List[dict[str, str]]:

    return [
        {
            "role": "system",
            "content": f"""You are a Aircraft Maintenance Engineer, your job is to assign a ATA code to each fault.\n
            Here are the details of how ATA are assigned:\n{details}""",
        },
        {
            "role": "user",
            "content": f"""Please assign a ATA to the fault: {fault}.
            Give your answer in the following format: ATA-XX where XX is the ATA code.
            """,
        },
    ]

# Initialize the HuggingFacePipeline with the specified model, task, and pipeline arguments
llm = HuggingFacePipeline.from_model_id(
        model_id="microsoft/Phi-3-mini-128k-instruct",  # The model to be used
        task="text-generation",  # The task to be performed
        pipeline_kwargs={
            "max_new_tokens": 1024,  # The maximum length of the generated text
        },
        device_map="auto",  # Automatically select the device to run the model on
    )

# The @traceable decorator is used to track the execution of the function.
# It can be used for logging, debugging, or performance monitoring.
@traceable
def invoke_llm(messages: List[dict[str, str]]) -> Any:
    # Invoke the HuggingFacePipeline with the provided messages and return the result
    return llm.invoke(messages)


def main():

    # Print a message to indicate the start of the grading process
    print("Running COPA ATA LLM ...")

    examples = load_examples("faults.csv",50)
    details = load_ATA_info()
    
    messages = format_prompt(
        details=details,
        example=examples,
        fault="BIRD STRIKE,DURING WALK AROUND BIRD STRIKE WAS NOTICED ON SIDE OF THE FUSELAGE",
    )

    # Invoke the language model to grade the student's answer
    response = invoke_llm(messages)
    print("Response is: ", response)


if __name__ == "__main__":
    main()
