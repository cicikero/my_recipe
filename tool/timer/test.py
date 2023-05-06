from stop_watch import stop_watch

@stop_watch
def func() :
    a=0
    for i in range(999999) :
        a+=i*i
    print(a)

func()
