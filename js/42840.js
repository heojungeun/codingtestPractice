function solution1(answers) {
    let answer = [];
    var lena = answers.length;
    var p1 = [1,2,3,4,5];
    var p2 = [2,1,2,3,2,4,2,5];
    var p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    function max(a,b){
      if(a>b) return a;
      else return b;
    }
    let value = 0;
    let cnt = [0,0,0];
    for (var i=0; i<lena;i++){
      if(p1[i%5]===answers[i]) cnt[0]++;
      if(p2[i%8]===answers[i]) cnt[1]++;
      if(p3[i%10]===answers[i]) cnt[2]++;
    }
    value = max(max(cnt[0],cnt[1]),cnt[2]);
    var idx = 0;
    for (var i=0;i<3;i++){
      if(cnt[i]===value){
        answer[idx] = i+1;
        idx += 1;
      }
    }
    return answer;
}

function solution(answers){
  var answer = [];
  var p1 = [1,2,3,4,5];
  var p2 = [2,1,2,3,2,4,2,5];
  var p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  var a1c = answers.filter((a,i)=> a === p1[i%5]).length;
  var a2c = answers.filter((a,i)=> a === p2[i%8]).length;
  var a3c = answers.filter((a,i)=> a === p3[i%10]).length;
  var max = Math.max(a1c,a2c,a3c);

  if (a1c===max){answer.push(1)};
  if (a2c===max){answer.push(2)};
  if (a3c===max){answer.push(3)};

  return answer
}

var asw = [1,2,3,4,5];
console.log(solution(asw));
