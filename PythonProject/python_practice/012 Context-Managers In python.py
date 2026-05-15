# Context manager - concept thet includes custom functionality before and after your main code.
# @contextlib.contextmanager
#
#
# def ef_context_manager():
#     print('---Before---')
#
#     # CODE BEFORE--
#
#     yield
#
#     # 🫴 CODE AFTER
#     print('---After---')
#
# with ef_context_manager():
#     print('---Test---')

# def time_it():
#     start = time.time() # Before-----
#     yield
#     end  = time.time()  # After------
#     timer = end - start
#     print(f'Time take: {timer:.6f}s')
# # Loop-------------------
# with time_it():
#     result = []
#     for i in range(10000):
#         result.append(i * 2)
#
# # Comprehension----------
# with time_it():
#     result = [i * 2 for i in range(10000)]
import contextlib,traceback

# def try_except(deb = False):
#     try:
#         yield
#     except:
#         if deb:
#            print(traceback.format_exc())
#
# with try_except(deb = True):
#     print(1/0)
# with try_except():
#     print(1/0)
@contextlib.contextmanager
def logger():
    print('ተጀመረ')
    yield
    print('ተጠናቀቀ')
with logger():
    print('ዋናው ሥራ እየተሠራ ነው...')

    # second code block-------------------------


@contextlib.contextmanager
def list_transaction(my_list, item):
    my_list.append(item)
    try:
        yield
    except Exception:
        my_list.remove(item)
        print('ስህተት ተፈጥሯል፣ ዳታው ተሰርዟል!')

number = [1, 2, 3]
with list_transaction(number, 4):
    print(10/0)
    print(number)