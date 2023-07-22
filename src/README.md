# Extractive Text Summarization - Configurations

![Extractive Text Summarizer - Configurations][config-screenshot]

The **`config.ini`** file is a simple text-based configuration file that contains key-value pairs. Each line in the file represents a configuration setting, where the key and value are separated by an equal sign (=). The file is designed to store various configuration parameters for the Python application.

## Trial Run configuration [Trial-Run]

This configuration is used to check the local setup for the extractive text summarization. It includes the following parameters:

| **Parameter** | **Acceptable Values** |                       **Description**                       |
|:-------------:|:---------------------:|:-----------------------------------------------------------:|
|   is_enabled  |      True / False     | Indicates whether the user want to execute Trial-Run or not |
|   input_path  |    Path-to-file.txt   |               Includes the Trial-Run file path              |


## Custom Run configuration [Custom-Run]

This configuration is used to execute the summarization process based on user preferences. It is **`only used if the Trial-Run configuration is set to False`**. It includes the following parameters:

| **Parameter** |                **Acceptable Values**                |                        **Description**                        |
|:-------------:|:---------------------------------------------------:|:-------------------------------------------------------------:|
|   input_type  |                   TEXT-FILE / URL                   |  Indicates the user input i.e. either text file or URL-based  |
|   input_path  |                   Path-to-file.txt                  |     Includes the Custom-Run file path or the article's URL    |
|   algorithm   | INTEGRATED / TEXT-RANK / BM25 / TF-IDF-COSINE / LCS | User's choice for the extractive text summarization algorithm |


## Rouge Score configuration [Rouge-Score]

This configuration is used to evaluate the results of the extractive summarization process. The Rouge-Score is **`only evaluated if there exists a human-generated summary for the same text input`**. It includes the following parameters:

|          **Parameter**         | **Acceptable Values** |                         **Description**                         |
|:------------------------------:|:---------------------:|:---------------------------------------------------------------:|
|           is_enabled           |      True / False     | Indicates whether the user want to evaluate Rouge Scores or not |
|  human_generated_summary_path  |    Path-to-file.txt   |          Includes the human-generated summary file path         |
| machine_generated_summary_path |    Path-to-file.txt   |         Includes the machine-generated summary file path        |

## Output configuration [Output]

This configuration allows the user to select the output type for the summarization process. It includes the following parameters:

| **Parameter** | **Acceptable Values** |                                     **Description**                                    |
|:-------------:|:---------------------:|:--------------------------------------------------------------------------------------:|
|  output_type  |     FILE / DISPLAY    | Indicates whether the user want to save the summary in a file or display it in console |
|  output_path  |    Path-to-file.txt   |                    Used only in case of **`File output_type`** mode                    |

<br />
<br />
<hr>

<!-- MARKDOWN LINKS & IMAGES -->
[config-screenshot]: data/assets/config.png
