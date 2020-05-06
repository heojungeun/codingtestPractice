function solution(n, lost, reserve) {
    var answer = n-lost.length;
    var lostmp = [];
    for(var i=0;i<lost.length;i++){
      lostmp.push(lost[i]);
    }
    for(var i=0;i<lost.length;i++){
      var x = lost[i];
      if(reserve.indexOf(x)!= -1){
        answer += 1;
        var idx = reserve.indexOf(x);
        reserve.splice(idx, 1);
        idx = lostmp.indexOf(x);
        lostmp.splice(idx, 1);
      }
    }
    for(var i=0;i<lostmp.length;i++){
      var x = lostmp[i];
      for(var j=0;j<reserve.length;j++){
        var y = reserve[j];
        if(y==x-1 || y==x+1){
          answer += 1;
          var idx = reserve.indexOf(y);
          reserve.splice(idx,1);
          break;
        }
      }
    }

    return answer;
}

var num = 5;
var lst = [2,4];
var rev = [1,3,5];
console.log(solution(num,lst,rev));
