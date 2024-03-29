# Extractive Text Summarization - Driver Code
#--------------------------------------------#

import configparser, requests, bs4, sys
from utils import constant, summarization, rouge
from os.path import abspath
import nltk

def validate_configuration(config_dict):
    if type(config_dict.get("trial_run")) is not bool:
        return "Invalid trial_run configuration setting"
    
    if config_dict.get("algorithm") not in constant.ALGORITHM_SET:
        return "Invalid algorithm in the configuration setting"
    
    if config_dict.get("input_type") not in constant.INPUT_TYPE_SET:
        return "Invalid input_type configuration setting"
    
    if config_dict.get("output_type") not in constant.OUTPUT_TYPE_SET:
        return "Invalid output_type configuration setting"
    
    if type(config_dict.get("rouge_score")) is not bool:
         return "Invalid rouge_score configuration setting"

    return "success"

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    config_dict = dict()

    # Read values from the 'Trial-Run' section
    trial_run = config.getboolean('Trial-Run', 'is_enabled')
    trial_run_input = config.get('Trial-Run', 'input_path')

    # Read values from the 'Custom-Run' section
    input_type = config.get('Custom-Run', 'input_type')
    input_path = config.get('Custom-Run', 'input_path')
    algorithm = config.get('Custom-Run', 'algorithm')

    # Read values from the 'Rouge-Score' section
    rouge_score_generation = config.getboolean('Rouge-Score', 'is_enabled')
    human_generated_summary_path = config.get('Rouge-Score', 'human_generated_summary_path')
    machine_generated_summary_path = config.get('Rouge-Score', 'machine_generated_summary_path')

    # Read values from the 'Output' section
    output_type = config.get('Output', 'output_type')
    output_path = config.get('Output', 'output_path')

    # Preparing the Configuration Dict
    config_dict["trial_run"] = trial_run
    config_dict["file_path"] = trial_run_input if (trial_run) else input_path
    config_dict["algorithm"] = algorithm
    config_dict["input_type"] = constant.INPUT_TYPE_FILE if (trial_run) else input_type
    config_dict["rouge_score"] = rouge_score_generation
    config_dict["human_generated_summary_path"] = human_generated_summary_path
    config_dict["machine_generated_summary_path"] = machine_generated_summary_path
    config_dict["output_type"] = output_type
    config_dict["output_path"] = output_path

    # Display for Configuration settings
    print("\n\nRunning using the following User Configurations : ")
    print(f"--> TRIAL-RUN = {trial_run}")
    if(trial_run):
        print(f"--> TRIAL-RUN-FILE-PATH = {trial_run_input}")
        print(f"--> TRIAL-RUN-ALGORITHM = {constant.PROPOSED_ALGORITHM} (Proposed Algorithm)")
    else:
        print(f"--> INPUT-TYPE = {input_type}")
        print(f"--> ALGORITHM  = {algorithm}")
        print(f"--> FILE_PATH / URL = {input_path}")
    
    print(f"--> OUTPUT-TYPE = {output_type}")
    print(f"--> OUTPUT-PATH = {output_path}")
    print(f"--> ROUGE-SCORE = {rouge_score_generation}")
    print(f"--> HUMAN GENERATED SUMMARY = {human_generated_summary_path}")
    print(f"--> MACHINE GENERATED SUMMARY = {machine_generated_summary_path}")

    # Validating Configuration
    message = validate_configuration(config_dict)
    if(message != "success"):
        print(f"\nERROR: {message}")
        sys.exit(0)

    return config_dict


def take_input(config_dict):
    if(config_dict.get('input_type') == constant.INPUT_TYPE_FILE):
        file_location = config_dict.get("file_path")
        print(f"\nReading the file: {file_location}")
        with open(abspath(file_location), encoding="utf8") as f:
            text = "\n".join(f.readlines())

    elif(config_dict.get('input_type') == constant.INPUT_TYPE_URL):
        url = config_dict.get("file_path")
        print(f"\nAccessing the URL: {url}")
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        text = soup.text

    return text


def main():
    try:
        # Downloading the essential NLTK modules
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('wordnet')

        # Extractive Text Summarization Process
        config_dict = get_config()
        text = take_input(config_dict)
        algorithm = constant.PROPOSED_ALGORITHM if config_dict.get("trial_run") else config_dict.get('algorithm')
        print(f"Summarizing the text using {algorithm} algorithm")
        summary = summarization.summarize(text=text, algorithm=algorithm)
        summarization.write_output(config_dict, summary)

        # ROUGE-SCORE Evaluation
        if(config_dict.get("rouge_score")):
            rouge.calculate_rouge(config_dict.get("human_generated_summary_path"), config_dict.get("machine_generated_summary_path"))

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

