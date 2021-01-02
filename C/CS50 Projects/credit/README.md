<!-- omit in toc -->
# Credit

This application simply validates a credit card using a specific algorithm that most if not all banks use today.

## Usage

```C
$ ./credit
Number: //ENTER YOUR CREDIT CARD NUMBER HERE
//OUTPUT (Visa, Master, AmericanExpress, or InValid)
```

## Logic

This program works by implementing a famously known algorithm to detect which credit card has been inputted. This algorithm is called **Luhn's Algorithm**. Here is how it works:

You can determine if a credit card number is (syntactically) valid as follows:

1. Double every other digit, starting with the card number’s second-to-last digit. Add the product's digits to a sum variable.
2. Add the number's that weren't multiplied to the sum as well.
3. If the sum’s last digit is 0 or if the sum is divisible by 10, the number is Valid!

That’s kind of confusing, so let’s try an example with this Visa Number: 4003600000000014

1. Let’s first highlight every other digit, starting with the number’s second-to-last digit:

    **4**0**0**3**6**0**0**0**0**0**0**0**0**0**1**4

2. Now lets double each of these numbers:

    `(1 x 2) + (0 x 2) + (0 x 2) + (0 x 2) + (0 x 2) + (6 x 2) + (0 x 2) + (4 x 2)`

    `2 + 0 + 0 + 0 + 0 + 12 + 0 + 8`

3. Then, split any double digit number into 2 digits. (in this case 12):

    `2 + 0 + 0 + 0 + 1 + 2 + 0 + 8`

4. Adding those up we get `13`. Now, we add 13 to any number we didn't double:

    `13 + 4 + 0 + 0 + 0 + 0 + 3 + 0`

5. Adding those numbers. we get `20`. As you can see, 20 is in fact divisible by 10, therefore it is a valid card number.

As for deciding which credit card type this is, we usually look at the first 2 digits together of the card, as well as the number of digits in that card.

* If it is 15 digits, and starts with either 34 or 37, it is an American Express Card.
* If it's 16 digits and starts with either of 51, 52, 53, 54, or 55, it is a MasterCard.
* If it is 13 or 16 digits and starts with 4, it is a Visa
