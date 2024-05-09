type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
  const filteredArr: number[] = []
  for (let i=0; i < arr.length; i++) {
    if (Boolean(fn(arr[i], i)) === true) {
      filteredArr.push(arr[i])
    }
  }
  return filteredArr
};