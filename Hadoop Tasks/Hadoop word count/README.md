Word Count: Count the occurrence of all the words in an input text file.

To run the script on a file make sure you have the file on the same dir

1. **Run the mapper and save output:**
   ```bash
   cat The_Book_of_Boba_Fett.txt | python3 mapper.py > mapper_output.txt
   ```

2. **Sort the mapper output:**
   ```bash
   sort mapper_output.txt > sorted_output.txt
   ```

3. **Run the reducer and save output:**
   ```bash
   cat sorted_output.txt | python3 reducer.py > final_output.txt
   ```

4. **View the final output:**
   ```bash
   cat final_output.txt
   ```