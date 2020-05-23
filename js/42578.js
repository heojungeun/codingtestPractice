function solution(clothes) {
    let answer = 1;
    const obj = {};
    for(let arr of clothes){
      obj[arr[1]] = (obj[arr[1]] || 0) + 1;
    }
    for(let key in obj){
      answer *= (obj[key]+1);
    }
    return answer - 1;
}

var _cloth = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]];
console.log(solution(_cloth));
