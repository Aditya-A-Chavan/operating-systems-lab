size = int(input("Enter the size of the page: "))
ref_pages = input("Enter the reference pages: ").split()

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]

def least_recently_used(size, ref_pages):
    faults = 0
    hits = 0
    pages = []

    for ref_page in ref_pages:
        if ref_page in pages:
            hits += 1
            pages.remove(ref_page)
            pages.append(ref_page)
        else:
            faults += 1
            if len(pages) < size:
                pages.append(ref_page)
            else:
                pages.remove(pages[0])
                pages.append(ref_page)

    print(f"Misses: {faults}")
    print(f"Hits: {hits}")
    
    return    


print("Least Recently Used:")
least_recently_used(size, test)


from queue import Queue

def first_in_first_out(ref_pages, size):
    faults = 0
    hits = 0

    pages = []

    for ref_page in ref_pages:
        if ref_page in pages:
            hits += 1
        else:
            faults += 1
            if len(pages) < size:
                pages.append(ref_page)
            else:
                pages.remove(pages[0])
                pages.append(ref_page)
    print(f"Misses: {faults}")
    print(f"Hits: {hits}")
    return


print("\nFirst In First Out:")
first_in_first_out(test, size)


def optimal_page_reload(ref_pages, size):
    def predict_page_to_be_replaced(index, pages, ref_pages):
        res = -1
        farthest = index

        for i in range(len(pages)):
            found = False
            for j in range(index, len(ref_pages)):
                if pages[i] == ref_pages[j]:
                    found = True
                    if j > farthest:
                        farthest = j
                        res = i
                    break
            
            if not found:
                return i

        if res == -1:  
            return 0
        else:
            return res

    def replacement(ref_pages, size):
        pages = []
        hits = 0
        faults = 0

        for i in range(len(ref_pages)):
            if ref_pages[i] in pages:
                hits += 1
                continue

            if len(pages) < size:
                faults += 1
                pages.append(ref_pages[i])
            else:
                faults += 1
                j = predict_page_to_be_replaced(i+1, pages, ref_pages)
                pages[j] = ref_pages[i]

        print(f"Misses: {faults}")
        print(f"Hits: {hits}")
        return

    replacement(test, size)


test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
print("\nOptimal Page Replacement:")
optimal_page_reload(test, size)
    
