public class BubbleSort{
    // Inefficent for large data sets, mostly used for educational purposes
    public static void main (String[] args){
        int[] array = {4,7,3,9,6,2};
        bubbleSort(array);
        for(int i: array){
            System.out.print(i + " ");
        }
    }

    public static void bubbleSort(int[] array){
        int length = array.length;

        for(int i=0; i< length-1; i++){
            boolean swapped = false;
            for(int j=0; j< length-i-1; j++){
                int leftElement = array[j];
                int rightElement = array[j+1];

                // swap left and right element if left is higher
                if(leftElement > rightElement){
                    array[j] = rightElement;
                    array[j+1] = leftElement;
                    swapped = true;
                }

            }
            if(!swapped) {break;}
        }
    }
}