function getall(el) {
    if(el.checked == true)
        return location.href = ('?shopsort='+el.value+'&opt=add');
    else  return location.href = ('?shopsort='+el.value+'&opt=del');
}


