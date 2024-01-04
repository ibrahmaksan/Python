
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Diziyi ikiye böl

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Sol yarıyı sırala
        merge_sort(right_half)  # Sağ yarıyı sırala

        i = j = k = 0

        # İki alt diziyi birleştir
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Eğer sol yarıdan eleman kalmışsa
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Eğer sağ yarıdan eleman kalmışsa
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1













