def function(list,index):
    try:
        list[index]
    except IndexError:
        print("Element not found")
    finally:
        print("Task completed")
function([1,2,3],1)