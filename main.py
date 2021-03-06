
import time
from edgar_utils import load_config
from Worker import Worker

def main():
    config = load_config()
    company_list_file = "data/inputs/NYSE.csv"
    worker = Worker(config, company_list_file)

    # Last test (10AM, 6/29): 31 companies in 75 seconds
    # Last test (10AM, 6/29): 2 companies in 16.8 seconds

    fetch_start = time.time()
    worker.fetch_companies()
    fetch_end = time.time()

    print('\n'*2, '='*3, "Performance", '='*3, "\n", len(worker.companies),"companies in", fetch_end - fetch_start, "seconds" ,'\n'*2)

    for company in worker.companies:
        num_statements = len(company.statements)
        num_sections = sum([len(statement.sections) for statement in company.statements])

        print(company.name, "yielded...")
        print("\t Statements:", num_statements)
        print("\t Sections:", num_sections)

if __name__ == "__main__":
    main()
