func fibonacci(number: Int) -> (Int){
     var a = 0
     var b = 1
    for _ in 0 ..< number { 
    	let temp = a
    	a = b
    	b = temp + b
    }
return a
}