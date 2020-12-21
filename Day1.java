package DayOne;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class PuzzleOne {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Integer entry1 = 0;
		
		Integer result = 0;
		
		ArrayList<Integer> expensesList = new ArrayList<Integer>();
		
		File expensesFile = new File("D:\\OneDrive\\Documents\\AdventOfCode\\day1-puzzle1.txt");
		
		//Creating a scanner to read the file
		Scanner scanner;
		try {
			scanner = new Scanner(expensesFile);
			
			while(scanner.hasNextLine() && scanner.hasNextInt()) {
				expensesList.add(scanner.nextInt());
			}
			
			for(int i = 0; i < expensesList.size(); i++) {
				entry1 = expensesList.get(i);
				for(Integer j = 0; j < expensesList.size(); j++) {
					if(!j.equals(i) ) {
						for(Integer k = 0; k < expensesList.size(); k++) {
							if(!k.equals(j) && !k.equals(i)) {
								entry1 += expensesList.get(j) + expensesList.get(k);
								if(entry1.equals(2020)) {
									result = expensesList.get(i) * expensesList.get(j) * expensesList.get(k); 
								}
								entry1 = expensesList.get(i);
							}
						}
					}
				}
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
