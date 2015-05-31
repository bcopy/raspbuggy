function Raspbuggy() {
  this.statusTimer = null;
  this.statusUpdateCallbacks = [];
}


Raspbuggy.prototype.start = function(){
    console.log( "Started");
    this.invokeGetStatusTimeout();
};

Raspbuggy.prototype.addStatusUpdateCallback = function(listener){
    this.statusUpdateCallbacks.push(listener);
};

Raspbuggy.prototype.invokeGetStatusTimeout = function(){
    raspbuggy.updateStatus();
    
    raspbuggy.statusTimer = setTimeout(function(){raspbuggy.invokeGetStatusTimeout()}, 3000);
};

Raspbuggy.prototype.updateStatus= function() {
  $.getJSON( "/status", function(reply) {
    console.log( "Raspbuggy Status > Running? "+reply.running+" Exit Code : " +reply.exitCode );
    
    $.each(raspbuggy.statusUpdateCallbacks, function( cb){
            try{
                this(reply);
            }catch(err){
                console.log("Could not update service status : "+err);
            }
    }, reply);

  })
  .fail(function() {
    console.log( "error : Could not obtain raspbuggy  status." );
    $.each(raspbuggy.statusUpdateCallbacks, function( cb ){
            try{
                this({running: -3, exitCode: -1});
            }catch(err){
                console.log("Could not update service status : "+err);
            }
    });
   

  });
};


Raspbuggy.prototype.executeScript= function(scriptContents) {
  $.ajaxSetup({ 
    contentType: "application/json"
  });
  $.post( "/execute","{\"scriptText\":\"import time\\nprint 'hello world'\\ntime.sleep(10)\"}", function(reply) {
    if(reply.success){
      // Update the status immediately
      raspbuggy.updateStatus();
    }else{
      window.alert("Script execution failed : "+reply.message);
    }
  },"json");
//  .fail(function() {
//    console.log( "error : Could not execute raspbuggy script." );
//  });
};

raspbuggy = new Raspbuggy();
