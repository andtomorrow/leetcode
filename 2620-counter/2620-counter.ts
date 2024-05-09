function createCounter(n: number): () => number {
    let r: number = n - 1
    return () => {
        r += 1
        return r
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */