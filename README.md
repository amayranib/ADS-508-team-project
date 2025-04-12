# Optimizing Workplace Health Policies Through Predictive Analytics With AWS

ADS508 - Cloud Computing  
Team 1

## Installation

To get started with this project, please clone the repository into your local machine using the commands below:

```bash
> git clone https://github.com/amayranib/ADS-508-team-project.git
> cd ADS-508-team-project
```

### Environment Setup

Run the notebooks in `env_setup/` to setup the Sagemaker Studio environment for this project. 

### Pipeline

To execute the pipeline, run the code in the notebook `/code_library/master_notebook.ipynb`. 
This will sequentially run all notebooks in the pipeline. 

## Contributors

**Company Name**: Lunara Tech  
**Industry**: Business Intelligence for HR & Employee Benefits  
**Size**: 200

- [Amayrani Balbuena](https://github.com/amayranib)
- [Jun Clemente](https://github.com/junclemente)
- [Lorena Dorado](https://github.com/renaqd)

## Methods

- Exploratory Data Analysis
- Pre-processing
- Data Visualization
- Statistical Modeling

## Technologies

- Amazon Web Services:
  - Sagemaker
  - Athena
  - S3
- Jupyter Notebook
- Python / Pandas
- Google Docs
- Generative AI
   - ChatGPT

## Abstract

Our team will analyze the impact of sick leave policies, vaccination rates, and flexible work arrangements on workplace health outcomes and productivity. Using predictive modeling, we aim to identify optimal policy configurations that balance employee well-being with business performance.

## Problem Statement

Our team represents the data science department at Lunara Tech, a consulting firm specializing in workplace health policy optimization. Our company wants to redesign their health policies to improve productivity and retention while controlling costs. Using public datasets from the CDC, Bureau of Labor Statistics, and census data, we'll develop predictive models to determine the optimal combination of sick leave flexibility, vaccination incentives, and wellness programs that maximize ROI. Our goal is to provide actionable recommendations on policy design and implementation that balances employee wellbeing with business outcomes.

### Goals

1. Work policy optimization: develop recommendations for sick leave, wellness programs, and work schedule accommodations from statistical analysis of public datasets. This would improve employee well-being while aligning with business goals.
2. Productivity Enhancement: provide metrics that show how workplace health policies impact missed work days, team engagement, and overall workforce efficiency to maximize productivity.
3. Cost Efficiency & ROI Maximization: develop a predictive model for policy ROI. The machine learning model will predict the financial return on investment for different combinations of sick leave, vaccination programs, and wellness initiatives based on company characteristics.

### Non-Goals

1. Individual Employee Health Tracking: Data collection will not involve personally identifiable health data of employees.
2. Legal Compliance Advisory: Legal guidance on labor laws, OSHA or Cal/OSHA requirements, or healthcare regulation will not be provided.
3. Medical or Clinical Recommendations: Medical treatments, vaccination protocols, or individual health interventions will not be prescribed or evaluated.

## Data Sources

1. CDC/National Center for Health Statistics

   - Source: [https://www.cdc.gov/nchs/nhis/documentation/2023-nhis.html](https://www.cdc.gov/nchs/nhis/documentation/2023-nhis.html)
   - Description: CDC National Health Interview Survey (NHIS)
   - Size: ~30,000+ records annually; 534-647 variables

2. U.S. Bureau of Labor Statistics

   - Source: [https://www.bls.gov/ebs/publications/annual-benefits-summary.htm](https://www.bls.gov/ebs/publications/annual-benefits-summary.htm)
   - Description: Bureau of Labor Statistics (BLIS) Employee Benefits Survey
   - Size: Data from 15,000+ establishments, 24 variables

3. University of Wisconsin Population Health Institute
   - Source: [https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation](https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation)
   - Description: County Health Rankings Dataset
   - Size: 3,000+ US Counties, 500-700+ variables

## Acknowledgments

Portions of this codebase and documentation were developed with assistance from ChatGPT (OpenAI), April 2025.

## References

- CDC (2024). 2023 NHIS questionnaires, datasets, and documentation. National Center for Health Statistics. https://www.cdc.gov/nchs/nhis/documentation/2023-nhis.html
- Fregly, C., & Barth, A. (2021). Data science on AWS. O'Reilly.
- Fregly, C., Barth, A., & Eigenbrode, S. (2023). Generative AI on AWS. O'Reilly.

## Presentations and Projects

- Video Presentation: [Link to Canva Presentation]
- Project Notebook: [Code Library Folder](code_library)
