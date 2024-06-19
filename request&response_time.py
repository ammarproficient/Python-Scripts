import requests
import time

while True:
    def check_internet_connection(url='https://www.google.com'):
        try:
            # Start time
            start_time = time.time()
            #  Response
            response = requests.get(url)

            # Calculate the total time taken for the request
            total_time = time.time() - start_time

            # Check the status code of the response
            if response.status_code == 200:
                print('Internet Connection Established')
            elif response.status_code == 404:
                print('Internet Connection Problem: Page Not Found (404)')
            else:
                print(f'Error: Received status code {response.status_code}')

            # Print the time taken for the request
            print(f'Request Time taken: {total_time:.2f} seconds')

        except requests.RequestException as e:
            # Handle any exceptions that occur during the request
            print(f'An error occurred: {e}')
            print("There is an error while connecting to the internet.")


    # Call the function
    check_internet_connection()
    time.sleep(1)
