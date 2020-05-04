function solution(participant, completion) {
    participant.sort();
    completion.sort();
    for(var i=0;i<participant.length;i++){
      if (participant[i] !== completion[i]){
        return participant[i];
      }
    }
}
var parti = ["leo", "kiki", "eden"];
var compl = ["eden","kiki"];
console.log(solution(parti, compl));
