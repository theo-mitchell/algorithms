public class NumberUtils {

  public static boolean isNarcissistic(int number) {
    char[] numbers = String.valueOf(number).toCharArray();
    int raisedNumbers[] = new int[numbers.length];
    int sum = 0;
    int power = numbers.length;

    for (int i = 0; i < numbers.length; i++) {
      int currentNumber = (int) Character.getNumericValue(numbers[i]);

      sum += (int) Math.pow(currentNumber, power);
    }

    return sum == number;
  };
}
