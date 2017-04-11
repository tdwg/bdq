var ieProfile = `<a href="#" class="list-group-item" style="text-align:left">
        <i class="fa fa-info fa-fw"></i> _NAME_
            <span class="pull-right text-muted small"><em>_DESC_</em></span>
    </a>`;    
var ieInserted = `<div class="list-group-item">
                                <a href="#" style="text-align:left">
                                    <i class="fa fa-info fa-fw"></i> _NAME_
                                </a>
                                <a href="javascript:deleteIE('_INDEX_')" style="text-align:left">
                                    <span class="pull-right text-muted small"><em><i style="color:red" class="fa fa-remove"></i></em></span>
                                </a>
                            </div>`;
var dimensionInserted = `<div class="list-group-item">
                                <a href="#" style="text-align:left">
                                    <i class="fa fa-info fa-fw"></i> _NAME_
                                </a>
                                <a href="javascript:deleteDimension('_INDEX_')" style="text-align:left">
                                    <span class="pull-right text-muted small"><em><i style="color:red" class="fa fa-remove"></i></em></span>
                                </a>
                            </div>`;
var dimensionProfile = `<a href="#" class="list-group-item" style="text-align:left">
    <i class="fa fa-info fa-fw"></i> _NAME_
        <span class="pull-right text-muted small"><em>_DESC_</em></span>
</a>`;

var criterionInserted = `<div class="list-group-item">
                                <a href="#" style="text-align:left">
                                    <i class="fa fa-info fa-fw"></i> _NAME_
                                </a>
                                <input id="criterion-value-_ID_" onkeyup="setCriterion(_INDEX_)" type="text"></input>
                            </div>`;
var criterionProfile = `<a href="#" class="list-group-item" style="text-align:left">
    <i class="fa fa-info fa-fw"></i> <span id="statement-_INDEX_">_NAME_</span> <strong><span id="criterion-_INDEX_">_CRITERION_</span></strong>
        <span class="pull-right text-muted small"><em></em></span>
</a>`;

var profile = {};
profile.useCase = {};
profile.vie = [];
profile.dqMeasurementPolicy = [];
profile.dqValidationPolicy = [];
profile.dqImprovementPolicy = [];

function setCriterion(index){    
    profile.dqValidationPolicy[index].criterion = $("#criterion-value-"+index).val();    
    $("#statement-"+index).html(profile.dqValidationPolicy[index].statement);
    $("#criterion-"+index).html(profile.dqValidationPolicy[index].criterion);
    
}
$("#i-use-case-name").keyup(function(){
    profile.useCase.name = $("#i-use-case-name").val();
    updateProfile();
});
$("#i-use-case-description").keyup(function(){
    profile.useCase.description = $("#i-use-case-description").val();
    updateProfile();
});    
function addCDimension(){        
    var cdimension = {
        dimension: $("#selected-dimension").val(),
        ie: $("#selected-ie").val(),
        drt: $("#selected-drt").val(),
        description: $("#i-cdimension-description").val()
    }
    profile.dqMeasurementPolicy.push(cdimension);
    $("#i-cdimension-description").val("");
    
    profile.dqValidationPolicy.push({
        dimensionIndex: profile.dqMeasurementPolicy.length-1,
        ie: cdimension.ie,
        drt: cdimension.drt,
        statement: cdimension.dimension+" of "+cdimension.ie+" of "+cdimension.drt+" must be ",
        criterion: ""
    });
    updateProfile();
}
function addIE(){        
    var ie = {
        name: $("#i-ie-name").val(),
        description: $("#i-ie-description").val(),
        dwc: $("#i-ie-dwc").val()
    }        
    profile.vie.push(ie);
    $("#i-ie-name").val("");
    $("#i-ie-description").val("");
    $("#i-ie-dwc").val("");
    updateProfile();
}
function deleteIE(index){
    profile.dqMeasurementPolicy = profile.dqMeasurementPolicy.filter(function(item){
        var rs = item.ie != profile.vie[index].name;            
        return rs;
    });       

    var i = 0;
    profile.vie = profile.vie.filter(function(item){
        var rs = i != index;
        i++;
        return rs;
    });    
    updateProfile();
}
function deleteDimension(index){
    var i = 0;
    profile.dqMeasurementPolicy = profile.dqMeasurementPolicy.filter(function(item){
        var rs = i != index;
        i++;
        return rs;
    });        
    updateProfile();
}
function updateProfile(){
    $("#l-use-case-name").html("DQ Profile for "+profile.useCase.name);
    $("#l-use-case-description").html(profile.useCase.description);
    $("#selected-ie").html('<option>Select an IE...</option>');        

    // IE
    var vieContent = "";
    var vieCreated = "";        
    var i = 0;        
    profile.vie.forEach(function(ie){            
        vieContent = vieContent + ieProfile.replace("_NAME_",ie.name).replace("_DESC_",ie.description)
        vieCreated = vieCreated + ieInserted.replace("_NAME_",ie.name).replace("_INDEX_",i)
        $("#selected-ie").append('<option value="'+ie.name+'">'+ie.name+'</option>');
        i++;
    });
    $("#vie-content").html(vieContent);
    $("#vie-created").html(vieCreated);
    
    // Dimension
    var dqMeasurementPolicyContent = "";
    var dqMeasurementPolicyCreated = "";        
    i = 0;        
    profile.dqMeasurementPolicy.forEach(function(dimension){            
        dqMeasurementPolicyContent = dqMeasurementPolicyContent + dimensionProfile.replace("_NAME_",dimension.dimension+" of "+dimension.ie+" of "+dimension.drt).replace("_DESC_",dimension.description);
        dqMeasurementPolicyCreated = dqMeasurementPolicyCreated + dimensionInserted.replace("_NAME_",dimension.dimension+" of "+dimension.ie+" of "+dimension.drt).replace("_INDEX_",i);
        i++;
    });
    $("#dq-measurement-policy-content").html(dqMeasurementPolicyContent);
    $("#dq-measurement-policy-created").html(dqMeasurementPolicyCreated);

    // Criterion
    var dqValidationPolicyContent = "";
    var dqValidationPolicyCreated = "";        
    i = 0;        
    profile.dqValidationPolicy.forEach(function(criterion){            
        dqValidationPolicyContent = dqValidationPolicyContent + criterionProfile.replace("_NAME_",criterion.statement+" ").replace("_CRITERION_",criterion.criterion).replace("_INDEX_",i).replace("_INDEX_",i);
        dqValidationPolicyCreated = dqValidationPolicyCreated + criterionInserted.replace("_NAME_",criterion.statement+" ").replace("_ID_",i).replace("_INDEX_",i);
        i++;
    });
    $("#dq-validation-policy-content").html(dqValidationPolicyContent);
    $("#dq-validation-policy-created").html(dqValidationPolicyCreated);
}    
function save(){
    if(localStorage) localStorage.profile = JSON.stringify(profile);
    else alert("Sorry, this resource doen't work in your Internet browser.");  
}

if (localStorage && localStorage.profile) {        
    profile = JSON.parse(localStorage.profile);    
    $("#i-use-case-name").val(profile.useCase.name);
    $("#i-use-case-description").val(profile.useCase.description);
}
    
updateProfile();