function Raspbuggy() {
  this.statusTimer = null;
}


Raspbuggy.prototype.start = function(){
    console.log( "Started");
};

Raspbuggy.prototype.invokeGetStatusTimeout = function(){
    var reply = raspbuggy.getStatus();
    raspbuggy.statusTimer = setTimeout(function(){raspbuggy.invokeGetStatusTimeout()}, 3000);
};

Raspbuggy.prototype.getStatus= function() {
  var result;
  $.getJSON( "/status", function(reply) {
    result = reply;
    console.log( "Raspbuggy Status > Running? "+reply.running+" Exit Code : " +reply.exitCode );
  })
  .fail(function() {
    console.log( "error : Could not obtain raspbuggy service status." );
  });
  return result;
};


Raspbuggy.prototype.executeScript= function() {
  $.getJSON( "/execute", function(reply) {
    if(reply.success){
      
    }else{
        
    }
  })
  .fail(function() {
    console.log( "error : Could not obtain raspbuggy service status." );
  });
};

raspbuggy = new Raspbuggy();
