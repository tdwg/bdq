class DQProfiler {  
    constructor() {
        var self = this;
        this.useCase = {};
        this.vie = [];
        this.dqMeasurementPolicy = {};
        this.dqValidationPolicy = {};
        this.dqImprovementPolicy = {};
        $("#i-use-case-name").keyup(self.setUseCaseName);                    
        $("#i-use-case-description").keyup(self.setUseCaseDesc);
        if (localStorage && localStorage.profile) {
            var profile = JSON.parse(localStorage.profile);            
            this.useCase = profile.useCase;
            this.vie = profile.vie;
            this.dqMeasurementPolicy = profile.dqMeasurementPolicy;
            this.dqValidationPolicy = profile.dqValidationPolicy;
            this.dqImprovementPolicy = profile.dqImprovementPolicy;
            $("#i-use-case-name").val(this.useCase.name);
            $("#i-use-case-description").val(this.useCase.description);
            this.updateProfile();
            this.updatePolicy();
        }
        $.widget.bridge('uitooltip', $.ui.tooltip);                
        var options = {
            items: "[title]",
            content: function() {
                var element = $( this );
                if ( element.is( "[title]" ) ) {                            
                    return element.attr( "title" );        
                }
            },
            position: {
                my: "center top",
                at: "bottom+15",
                collision: "none"
            }                    
        }
        $(document).uitooltip(options);
    }
    save(){
        var profile = {
            useCase:this.useCase,
            vie:this.vie,
            dqMeasurementPolicy:this.dqMeasurementPolicy,
            dqValidationPolicy:this.dqValidationPolicy,
            dqImprovementPolicy:this.dqImprovementPolicy
        }              
        if(localStorage) localStorage.profile = JSON.stringify(profile);        
        else alert("Sorry, this resource doen't work in your Internet browser.");  
    }
    setUseCaseName(){
        this.useCase.name = $("#i-use-case-name").val();
        this.updateProfile();
    }
    setUseCaseDesc(){
        this.useCase.description = $("#i-use-case-description").val();
        this.updateProfile();
    }
    htmlIEProfile(name,desc) {
        return `<a href="#" title="${desc}" class="list-group-item" style="text-align:left">
                    <i class="fa fa-info fa-fw"></i> ${name}            
                </a>`;
    }
    htmlIEInserted(name,desc,index) {
        return `<div class="list-group-item">
                    <a href="#" title="${desc}" style="text-align:left">
                        <i class="fa fa-info fa-fw"></i> ${name}
                    </a>
                    <a href="javascript:profiler.deleteIE('${index}')" style="text-align:left">
                        <span class="pull-right text-muted small"><em><i style="color:red" class="fa fa-remove"></i></em></span>
                    </a>
                </div>`;
    }
    htmlDimensionProfile(name,desc) {
        return `<a href="#" title="${desc}" class="list-group-item" style="text-align:left">
                    <i class="fa fa-info fa-fw"></i> ${name}        
                </a>`;
    }
    htmlCriterionProfile(name,desc,index,criterion) {
        return `<a href="#" title="${desc}" class="list-group-item" style="text-align:left">
                    <i class="fa fa-info fa-fw"></i> <span id="statement-${index}">${name}</span> <strong><span id="criterion-${index}">${criterion}</span></strong>
                        <span class="pull-right text-muted small"><em></em></span>
                </a>`;
    }
    htmlEnhancementProfile(name,desc,index,enhancement) {
        return `<a href="#" title="${desc}" class="list-group-item" style="text-align:left">
                    <i class="fa fa-info fa-fw"></i> <strong><span id="enhancement-${index}">${enhancement}</span></strong> for improving <span id="statement-${index}">${name}</span>
                        <span class="pull-right text-muted small"><em></em></span>
                </a>`;
    }
    addIE(){
        var self = this;
        var ie = {
            name: $("#i-ie-name").val(),
            description: $("#i-ie-description").val(),
            dwc: $("#i-ie-dwc").val()
        }        
        self.vie.push(ie);
        $("#i-ie-name").val("");
        $("#i-ie-description").val("");
        $("#i-ie-dwc").val("");
        self.updateProfile();
        self.updatePolicy();
    }
    deleteIE(index){
        var self = this;
        Object.keys(self.dqMeasurementPolicy).forEach(function(key){        
            if(self.dqMeasurementPolicy[key].ie==self.vie[index].name)
                delete self.dqMeasurementPolicy[key];
        });
        Object.keys(self.dqValidationPolicy).forEach(function(key){        
            if(self.dqValidationPolicy[key].ie==self.vie[index].name)
                delete self.dqValidationPolicy[key];
        });
        Object.keys(self.dqImprovementPolicy).forEach(function(key){        
            if(self.dqImprovementPolicy[key].ie==self.vie[index].name)
                delete self.dqImprovementPolicy[key];
        });
        var i = 0;
        self.vie = self.vie.filter(function(item){
            var rs = i != index;
            i++;
            return rs;
        });    
        self.updateProfile();
        self.updatePolicy();
    }
    addCDimension(dimension,ie,resourceType,description){
        var self = this;
        if(description && String(description).trim().length>0){
            var cdimension = {
                dimension: dimension,
                ie: ie,
                drt: resourceType,
                description: description
            }        
            self.dqMeasurementPolicy[`${dimension}-${ie}-${resourceType}`] = cdimension;    
            self.updateProfile();
        }    
    }    
    addCCriterion(dimension,ie,resourceType,description){
        var self = this;      
        if(description && String(description).trim().length>0){
            var ccriterion = {
                dimension: dimension,
                ie: ie,
                drt: resourceType,
                criterion: description
            }        
            self.dqValidationPolicy[`${dimension}-${ie}-${resourceType}`] = ccriterion;    
            self.updateProfile();
        }    
    }
    addCEnhancement(dimension,ie,resourceType,description){
        var self = this;      
        if(description && String(description).trim().length>0){
            var cenhancement = {
                dimension: dimension,
                ie: ie,
                drt: resourceType,
                enhancement: description
            }        
            self.dqImprovementPolicy[`${dimension}-${ie}-${resourceType}`] = cenhancement;    
            self.updateProfile();
        }    
    }
    updateProfile(){
        var self = this;
        $("#l-use-case-name").html(`DQ Profile for ${self.useCase.name}`);
        $("#l-use-case-description").html(self.useCase.description);
        $("#selected-ie").html('<option>Select an IE...</option>');                
        // Dimension
        var dqMeasurementPolicyContent = ``;
        Object.keys(self.dqMeasurementPolicy).forEach((key)=>{
            var name = `${self.dqMeasurementPolicy[key].ie} ${self.dqMeasurementPolicy[key].dimension.toLowerCase()} of ${self.dqMeasurementPolicy[key].drt}`,
            desc = self.dqMeasurementPolicy[key].description;
            dqMeasurementPolicyContent = dqMeasurementPolicyContent + self.htmlDimensionProfile(name,desc);        
        });        
        // Criterion
        var dqValidationPolicyContent = ``;    
        Object.keys(self.dqValidationPolicy).forEach((key)=>{            
            var name = `${self.dqValidationPolicy[key].ie} ${self.dqValidationPolicy[key].dimension.toLowerCase()} of ${self.dqValidationPolicy[key].drt} must be `,
                        desc = self.dqMeasurementPolicy[key]?self.dqMeasurementPolicy[key].description:"Undefined",
                        index = key,
                        criterion = self.dqValidationPolicy[key].criterion.toLowerCase();
            dqValidationPolicyContent = dqValidationPolicyContent + self.htmlCriterionProfile(name,desc,index,criterion);
        });
        // Enhancement
        var dqImprovementPolicyContent = ``;    
        Object.keys(self.dqImprovementPolicy).forEach((key)=>{            
            var name = `${self.dqImprovementPolicy[key].ie.toLowerCase()} ${self.dqImprovementPolicy[key].dimension.toLowerCase()} of ${self.dqImprovementPolicy[key].drt}`,
                        desc = self.dqMeasurementPolicy[key]?self.dqMeasurementPolicy[key].description:"Undefined",
                        index = key,            
                        enhancement = self.dqImprovementPolicy[key].enhancement;
            dqImprovementPolicyContent = dqImprovementPolicyContent + self.htmlEnhancementProfile(name,desc,index,enhancement);
        });
        $("#dq-measurement-policy-content").html(dqMeasurementPolicyContent);
        $("#dq-validation-policy-content").html(dqValidationPolicyContent);
        $("#dq-improvement-policy-content").html(dqImprovementPolicyContent);        
    }
    updatePolicy(){ 
        var self = this;
        var vieContent = "",
            vieCreated = "";           
        $( "#accordionSingle" ).html("");
        $( "#accordionMulti" ).html("");
        $( "#accordionSingle" ).accordion({
            heightStyle: "content",
            collapsible: true
        });
        $( "#accordionMulti" ).accordion({
            heightStyle: "content",
            collapsible: true
        });
        var i = 0;        
        self.vie.forEach((ie)=>{
            var name = ie.name,
                desc = `${ie.description} (${ie.dwc})`;
            vieContent = vieContent + self.htmlIEProfile(name,desc);
            vieCreated = vieCreated + self.htmlIEInserted(name,desc,i);
            $("#selected-ie").append(`<option value="${name}">${name}</option>`);        
            
                var contextualizedDimensions = [
                    {
                        id: "completeness",
                        name: "Completeness"                        
                    },
                    {
                        id: "conformance",
                        name: "Conformance"
                    },
                    {
                        id: "consistency",
                        name: "Consistency"
                    },
                    {
                        id: "accuracy",
                        name: "accuracy"
                    }
                ];
                var resourceTypes = [
                    "single records",
                    "multi records"
                ];
                resourceTypes.forEach((rt)=>{
                    $.get("assets/parts/dq-policy-input.html",(content)=>{
                        var c = $(content);
                        c.find("span[name='ie']").html(name);            
                        c.find("#defining-completeness").hide();
                        c.find("#defining-conformance").hide();
                        c.find("#defining-consistency").hide();
                        c.find("#defining-accuracy").hide();
                        c.find("span[name='resourceType']").html(rt);

                        contextualizedDimensions.forEach((cd)=>{                        
                                c.find(`#selected-${cd.id}`).change(function(){
                                    if($(this).val()=="Yes"){                    
                                        c.find(`#defining-${cd.id}`).slideDown();                    
                                        c.find(`#defining-${cd.id}`).find("#dimension").keyup(function(e){                                    
                                            self.addCDimension(cd.name,name,rt,$(this).val());
                                        });
                                        c.find(`#defining-${cd.id}`).find("#criterion").keyup(function(e){                                            
                                            self.addCCriterion(cd.name,name,rt,$(this).val());
                                        });
                                        c.find(`#defining-${cd.id}`).find("#enhancement").keyup(function(e){
                                            self.addCEnhancement(cd.name,name,rt,$(this).val());
                                        });
                                    } else {
                                        c.find(`#defining-${cd.id}`).slideUp();
                                    }
                                });
                                if(self.dqMeasurementPolicy[`${cd.name}-${name}-${rt}`]&&self.dqMeasurementPolicy[`${cd.name}-${name}-${rt}`].description){                            
                                    c.find(`#defining-${cd.id}`).find("#dimension").val(self.dqMeasurementPolicy[`${cd.name}-${name}-${rt}`].description);
                                    c.find(`#selected-${cd.id}`).val("Yes").trigger("change");
                                }
                                if(self.dqValidationPolicy[`${cd.name}-${name}-${rt}`]&&self.dqValidationPolicy[`${cd.name}-${name}-${rt}`].criterion){
                                    c.find(`#defining-${cd.id}`).find("#criterion").val(self.dqValidationPolicy[`${cd.name}-${name}-${rt}`].criterion);
                                    c.find(`#selected-${cd.id}`).val("Yes").trigger("change");
                                }
                                if(self.dqImprovementPolicy[`${cd.name}-${name}-${rt}`]&&self.dqImprovementPolicy[`${cd.name}-${name}-${rt}`].enhancement){
                                    c.find(`#defining-${cd.id}`).find("#enhancement").val(self.dqImprovementPolicy[`${cd.name}-${name}-${rt}`].enhancement);
                                    c.find(`#selected-${cd.id}`).val("Yes").trigger("change");
                                }                                                                         
                        });   


                        if(rt=="single records"){                            
                            $("#accordionSingle").append(c).accordion('refresh');             
                        } else {                            
                            $("#accordionMulti").append(c).accordion('refresh');
                        }    
                    });                                      
                });                   
            
            i++;
        });
        $("#vie-content").html(vieContent);
        $("#vie-content").uitooltip({
        show: {
            effect: "slideDown",
            delay: 250
        }
        });
        $("#vie-created").html(vieCreated);
        $("#vie-created").uitooltip({
        show: {
            effect: "slideDown",
            delay: 250
        }
        });
    }
}

var profiler = new DQProfiler();  
// console.log(profiler.getIeProfile("teste"));

// var ieProfile = `<a href="#" title="_DESC_" class="list-group-item" style="text-align:left">
//         <i class="fa fa-info fa-fw"></i> _NAME_            
//     </a>`;    
// var ieInserted = `<div class="list-group-item">
//                                 <a href="#" title="_DESC_" style="text-align:left">
//                                     <i class="fa fa-info fa-fw"></i> _NAME_
//                                 </a>
//                                 <a href="javascript:deleteIE('_INDEX_')" style="text-align:left">
//                                     <span class="pull-right text-muted small"><em><i style="color:red" class="fa fa-remove"></i></em></span>
//                                 </a>
//                             </div>`;

// var dimensionProfile = `<a href="#" title="_DESC_" class="list-group-item" style="text-align:left">
//     <i class="fa fa-info fa-fw"></i> _NAME_        
// </a>`;

// var criterionProfile = `<a href="#" title="_DESC_" class="list-group-item" style="text-align:left">
//     <i class="fa fa-info fa-fw"></i> <span id="statement-_INDEX_">_NAME_</span> <strong><span id="criterion-_INDEX_">_CRITERION_</span></strong>
//         <span class="pull-right text-muted small"><em></em></span>
// </a>`;

// var profile = {};
// profile.useCase = {};
// profile.vie = [];
// profile.dqMeasurementPolicy = {};
// profile.dqValidationPolicy = {};
// profile.dqImprovementPolicy = [];

// $("#i-use-case-name").keyup(function(){
//     profile.useCase.name = $("#i-use-case-name").val();
//     updateProfile();
// });
// $("#i-use-case-description").keyup(function(){
//     profile.useCase.description = $("#i-use-case-description").val();
//     updateProfile();
// });

// function addCDimension(dimension,ie,resourceType,description){        
//     if(description && String(description).trim().length>0){
//         var cdimension = {
//             dimension: dimension,
//             ie: ie,
//             drt: resourceType,
//             description: description
//         }        
//         profile.dqMeasurementPolicy[dimension+"-"+ie+"-"+resourceType] = cdimension;    
//         updateProfile();
//     }    
// }
// function addCCriterion(dimension,ie,resourceType,description){        
//     if(description && String(description).trim().length>0){
//         var ccriterion = {
//             dimension: dimension,
//             ie: ie,
//             drt: resourceType,
//             criterion: description
//         }        
//         profile.dqValidationPolicy[dimension+"-"+ie+"-"+resourceType] = ccriterion;    
//         updateProfile();
//     }    
// }
// function addIE(){
//     var ie = {
//         name: $("#i-ie-name").val(),
//         description: $("#i-ie-description").val(),
//         dwc: $("#i-ie-dwc").val()
//     }        
//     profile.vie.push(ie);
//     $("#i-ie-name").val("");
//     $("#i-ie-description").val("");
//     $("#i-ie-dwc").val("");    
//     updateProfile();
//     updatePolicy();
// }
// function deleteIE(index){
//     Object.keys(profile.dqMeasurementPolicy).forEach(function(key){        
//         if(profile.dqMeasurementPolicy[key].ie==profile.vie[index].name)
//             delete profile.dqMeasurementPolicy[key];
//     });
//     Object.keys(profile.dqValidationPolicy).forEach(function(key){        
//         if(profile.dqValidationPolicy[key].ie==profile.vie[index].name)
//             delete profile.dqValidationPolicy[key];
//     });
//     var i = 0;
//     profile.vie = profile.vie.filter(function(item){
//         var rs = i != index;
//         i++;
//         return rs;
//     });    
//     updateProfile();
//     updatePolicy();
// }
// function deleteDimension(index){
//     var i = 0;
//     profile.dqMeasurementPolicy = profile.dqMeasurementPolicy.filter(function(item){
//         var rs = i != index;
//         i++;
//         return rs;
//     });        
//     updateProfile();
// }
// function updatePolicy(){ 
//     var vieContent = "";
//     var vieCreated = "";           
//     $( "#accordionSingle" ).html("");
//     $( "#accordionMulti" ).html("");
//     $( "#accordionSingle" ).accordion({
//         heightStyle: "content",
//         collapsible: true
//     });
//     $( "#accordionMulti" ).accordion({
//         heightStyle: "content",
//         collapsible: true
//     });
//     var i = 0;
//     profile.vie.forEach(function(ie){
//         vieContent = vieContent + ieProfile.replace("_NAME_",ie.name).replace("_DESC_",ie.description+" ("+ie.dwc+")")
//         vieCreated = vieCreated + ieInserted.replace("_NAME_",ie.name).replace("_INDEX_",i).replace("_DESC_",ie.description+" ("+ie.dwc+")")
//         $("#selected-ie").append('<option value="'+ie.name+'">'+ie.name+'</option>');        
//         $.get("assets/parts/dq-policy-input.html",function(content){            
//             var c = $(content);
//             c.find("span[name='ie']").html(ie.name);            
//             c.find("#defining-completeness").hide();
//             c.find("#defining-conformance").hide();
//             c.find("#defining-consistency").hide();
//             c.find("#defining-accuracy").hide();
//             //  SINGLE
//             c.find("span[name='resourceType']").html("single records");            
//             // Completeness            
//             c.find("#selected-completeness").change(function(){                
//                 if($(this).val()=="Yes"){                    
//                     c.find("#defining-completeness").slideDown();                    
//                     c.find("#defining-completeness").find("#dimension").keyup(function(e){
//                         addCDimension("Completeness",ie.name,"single records",$(this).val());
//                     });
//                     c.find("#defining-completeness").find("#criterion").keyup(function(e){
//                         addCCriterion("Completeness",ie.name,"single records",$(this).val());
//                     });
//                 } else {
//                     c.find("#defining-completeness").slideUp();
//                 }
//             });
//             if(profile.dqMeasurementPolicy["Completeness-"+ie.name+"-single records"]&&profile.dqMeasurementPolicy["Completeness-"+ie.name+"-single records"].description){
//                 c.find("#defining-completeness").find("#dimension").val(profile.dqMeasurementPolicy["Completeness-"+ie.name+"-single records"].description);
//                 c.find("#selected-completeness").val("Yes").trigger("change");
//             }
//             if(profile.dqValidationPolicy["Completeness-"+ie.name+"-single records"]&&profile.dqValidationPolicy["Completeness-"+ie.name+"-single records"].criterion){
//                 c.find("#defining-completeness").find("#criterion").val(profile.dqValidationPolicy["Completeness-"+ie.name+"-single records"].criterion);
//                 c.find("#selected-completeness").val("Yes").trigger("change");
//             }            

//             // Conformance            
//             c.find("#selected-conformance").change(function(){
//                 if($(this).val()=="Yes"){
//                     c.find("#defining-conformance").slideDown();                    
//                     c.find("#defining-conformance").find("#dimension").keyup(function(e){                        
//                         addCDimension("Conformance",ie.name,"single records",$(this).val());
//                     });
//                     c.find("#defining-conformance").find("#criterion").keyup(function(e){                        
//                         addCCriterion("Conformance",ie.name,"single records",$(this).val());
//                     });
//                 } else {
//                     c.find("#defining-conformance").slideUp();
//                 }
//             });   
//             if(profile.dqMeasurementPolicy["Conformance-"+ie.name+"-single records"]&&profile.dqMeasurementPolicy["Conformance-"+ie.name+"-single records"].description){
//                 c.find("#defining-conformance").find("#dimension").val(profile.dqMeasurementPolicy["Conformance-"+ie.name+"-single records"].description);
//                 c.find("#selected-conformance").val("Yes").trigger("change");
//             }
//             if(profile.dqValidationPolicy["Conformance-"+ie.name+"-single records"]&&profile.dqValidationPolicy["Conformance-"+ie.name+"-single records"].criterion){
//                 c.find("#defining-conformance").find("#criterion").val(profile.dqValidationPolicy["Conformance-"+ie.name+"-single records"].criterion);
//                 c.find("#selected-conformance").val("Yes").trigger("change");
//             }
            
//             // Consistency
//             c.find("#selected-consistency").change(function(){
//                 if($(this).val()=="Yes"){
//                     c.find("#defining-consistency").slideDown();
//                     c.find("#defining-consistency").find("#dimension").keyup(function(e){
//                         addCDimension("Consistency",ie.name,"single records",$(this).val());
//                     });
//                     c.find("#defining-consistency").find("#criterion").keyup(function(e){
//                         addCCriterion("Consistency",ie.name,"single records",$(this).val());
//                     });
//                 } else {
//                     c.find("#defining-consistency").slideUp();
//                 }
//             });  
//             if(profile.dqMeasurementPolicy["Consistency-"+ie.name+"-single records"]&&profile.dqMeasurementPolicy["Consistency-"+ie.name+"-single records"].description){
//                 c.find("#defining-consistency").find("#dimension").val(profile.dqMeasurementPolicy["Consistency-"+ie.name+"-single records"].description);
//                 c.find("#selected-consistency").val("Yes").trigger("change");
//             }
//             if(profile.dqValidationPolicy["Consistency-"+ie.name+"-single records"]&&profile.dqValidationPolicy["Consistency-"+ie.name+"-single records"].criterion){
//                 c.find("#defining-consistency").find("#criterion").val(profile.dqValidationPolicy["Consistency-"+ie.name+"-single records"].criterion);
//                 c.find("#selected-consistency").val("Yes").trigger("change");
//             }

//             // Accuracy
//             c.find("#selected-accuracy").change(function(){
//                 if($(this).val()=="Yes"){
//                     c.find("#defining-accuracy").slideDown();
//                     c.find("#defining-accuracy").find("#dimension").keyup(function(e){
//                         addCDimension("Accuracy",ie.name,"single records",$(this).val());
//                     });
//                     c.find("#defining-accuracy").find("#criterion").keyup(function(e){
//                         addCCriterion("Accuracy",ie.name,"single records",$(this).val());
//                     });
//                 } else {
//                     c.find("#defining-accuracy").slideUp();
//                 }
//             });    
//             if(profile.dqMeasurementPolicy["Accuracy-"+ie.name+"-single records"]&&profile.dqMeasurementPolicy["Accuracy-"+ie.name+"-single records"].description){
//                 c.find("#defining-accuracy").find("#dimension").val(profile.dqMeasurementPolicy["Accuracy-"+ie.name+"-single records"].description);
//                 c.find("#selected-accuracy").val("Yes").trigger("change");
//             }
//             if(profile.dqValidationPolicy["Accuracy-"+ie.name+"-single records"]&&profile.dqValidationPolicy["Accuracy-"+ie.name+"-single records"].criterion){
//                 c.find("#defining-accuracy").find("#criterion").val(profile.dqValidationPolicy["Accuracy-"+ie.name+"-single records"].criterion);
//                 c.find("#selected-accuracy").val("Yes").trigger("change");
//             }

//             $("#accordionSingle").append(c).accordion('refresh');
            
//             // MULTI
//             var mc = c.clone();
//             mc.find("span[name='resourceType']").html("multi records");
//             // Completeness
//             mc.find("#selected-completeness").change(function(){
//                 if($(this).val()=="Yes"){
//                     mc.find("#defining-completeness").slideDown();
//                     c.find("#defining-completeness").find("#dimension").keyup(function(e){
//                         addCDimension("Completeness",ie.name,"multi records",$(this).val());
//                     });
//                     c.find("#defining-completeness").find("#criterion").keyup(function(e){
//                         addCCriterion("Completeness",ie.name,"multi records",$(this).val());
//                     });
//                 } else {
//                     mc.find("#defining-completeness").slideUp();
//                 }
//             });
//             if(profile.dqMeasurementPolicy["Completeness-"+ie.name+"-multi records"]&&profile.dqMeasurementPolicy["Completeness-"+ie.name+"-multi records"].description){
//                 c.find("#defining-completeness").find("#dimension").val(profile.dqMeasurementPolicy["Completeness-"+ie.name+"-multi records"].description);
//                 c.find("#selected-completeness").val("Yes").trigger("change");
//             }
//             if(profile.dqValidationPolicy["Completeness-"+ie.name+"-multi records"]&&profile.dqValidationPolicy["Completeness-"+ie.name+"-multi records"].criterion){
//                 c.find("#defining-completeness").find("#criterion").val(profile.dqValidationPolicy["Completeness-"+ie.name+"-multi records"].criterion);
//                 c.find("#selected-completeness").val("Yes").trigger("change");
//             }

//             // Conformance
//             mc.find("#selected-conformance").change(function(){
//                 if($(this).val()=="Yes"){
//                     mc.find("#defining-conformance").slideDown();
//                     c.find("#defining-conformance").find("#dimension").keyup(function(e){
//                         addCDimension("Conformance",ie.name,"multi records",$(this).val());
//                     });
//                     c.find("#defining-conformance").find("#criterion").keyup(function(e){
//                         addCCriterion("Conformance",ie.name,"multi records",$(this).val());
//                     });
//                 } else {
//                     mc.find("#defining-conformance").slideUp();
//                 }
//             });      
//             if(profile.dqMeasurementPolicy["Conformance-"+ie.name+"-multi records"]&&profile.dqMeasurementPolicy["Conformance-"+ie.name+"-multi records"].description){
//                 c.find("#defining-conformance").find("#dimension").val(profile.dqMeasurementPolicy["Conformance-"+ie.name+"-multi records"].description);
//                 c.find("#selected-conformance").val("Yes").trigger("change");
//             }
//             if(profile.dqValidationPolicy["Conformance-"+ie.name+"-multi records"]&&profile.dqValidationPolicy["Conformance-"+ie.name+"-multi records"].criterion){
//                 c.find("#defining-conformance").find("#criterion").val(profile.dqValidationPolicy["Conformance-"+ie.name+"-multi records"].criterion);
//                 c.find("#selected-conformance").val("Yes").trigger("change");
//             }

//             // Consistency
//             mc.find("#selected-consistency").change(function(){
//                 if($(this).val()=="Yes"){
//                     mc.find("#defining-consistency").slideDown();
//                     c.find("#defining-consistency").find("#dimension").keyup(function(e){
//                         addCDimension("Consistency",ie.name,"multi records",$(this).val());
//                     });
//                     c.find("#defining-consistency").find("#criterion").keyup(function(e){
//                         addCCriterion("Consistency",ie.name,"multi records",$(this).val());
//                     });
//                 } else {
//                     mc.find("#defining-consistency").slideUp();
//                 }
//             });  
//             if(profile.dqMeasurementPolicy["Consistency-"+ie.name+"-multi records"]&&profile.dqMeasurementPolicy["Consistency-"+ie.name+"-multi records"].description){
//                 c.find("#defining-consistency").find("#dimension").val(profile.dqMeasurementPolicy["Consistency-"+ie.name+"-multi records"].description);
//                 c.find("#selected-consistency").val("Yes").trigger("change");
//             }
//             if(profile.dqValidationPolicy["Consistency-"+ie.name+"-multi records"]&&profile.dqValidationPolicy["Consistency-"+ie.name+"-multi records"].criterion){
//                 c.find("#defining-consistency").find("#criterion").val(profile.dqValidationPolicy["Consistency-"+ie.name+"-multi records"].criterion);
//                 c.find("#selected-consistency").val("Yes").trigger("change");
//             }

//             // Accuracy
//             mc.find("#selected-accuracy").change(function(){
//                 if($(this).val()=="Yes"){
//                     mc.find("#defining-accuracy").slideDown();
//                     c.find("#defining-accuracy").find("#dimension").keyup(function(e){
//                         addCDimension("Accuracy",ie.name,"multi records",$(this).val());
//                     });
//                     c.find("#defining-accuracy").find("#criterion").keyup(function(e){
//                         addCCriterion("Accuracy",ie.name,"multi records",$(this).val());
//                     });
//                 } else {
//                     mc.find("#defining-accuracy").slideUp();
//                 }
//             });  
//             if(profile.dqMeasurementPolicy["Accuracy-"+ie.name+"-multi records"]&&profile.dqMeasurementPolicy["Accuracy-"+ie.name+"-multi records"].description){
//                 c.find("#defining-accuracy").find("#dimension").val(profile.dqMeasurementPolicy["Accuracy-"+ie.name+"-multi records"].description);
//                 c.find("#selected-accuracy").val("Yes").trigger("change");
//             }
//             if(profile.dqValidationPolicy["Accuracy-"+ie.name+"-multi records"]&&profile.dqValidationPolicy["Accuracy-"+ie.name+"-multi records"].criterion){
//                 c.find("#defining-accuracy").find("#criterion").val(profile.dqValidationPolicy["Accuracy-"+ie.name+"-multi records"].criterion);
//                 c.find("#selected-accuracy").val("Yes").trigger("change");
//             } 
//             $("#accordionMulti").append(mc).accordion('refresh');
//         });
//         i++;
//     });
//     $("#vie-content").html(vieContent);
//     $("#vie-content").uitooltip({
//       show: {
//         effect: "slideDown",
//         delay: 250
//       }
//     });
//     $("#vie-created").html(vieCreated);
//     $("#vie-created").uitooltip({
//       show: {
//         effect: "slideDown",
//         delay: 250
//       }
//     });
// }
// function updateProfile(){        
//     $("#l-use-case-name").html("DQ Profile for "+profile.useCase.name);
//     $("#l-use-case-description").html(profile.useCase.description);
//     $("#selected-ie").html('<option>Select an IE...</option>');                
//     // Dimension
//     var dqMeasurementPolicyContent = "";
//     Object.keys(profile.dqMeasurementPolicy).forEach(function(key){            
//         dqMeasurementPolicyContent = dqMeasurementPolicyContent + dimensionProfile.replace("_NAME_",profile.dqMeasurementPolicy[key].ie+" "+profile.dqMeasurementPolicy[key].dimension.toLowerCase()+" of "+profile.dqMeasurementPolicy[key].drt).replace("_DESC_",profile.dqMeasurementPolicy[key].description);        
//     });
//     $("#dq-measurement-policy-content").html(dqMeasurementPolicyContent).uitooltip({
//       show: {
//         effect: "slideDown",
//         delay: 250
//       }
//     });    
//     // Criterion
//     var dqValidationPolicyContent = "";    
//     Object.keys(profile.dqValidationPolicy).forEach(function(key){                  
//         dqValidationPolicyContent = dqValidationPolicyContent + criterionProfile.replace("_NAME_",profile.dqValidationPolicy[key].ie+" "+profile.dqValidationPolicy[key].dimension.toLowerCase()+" of "+profile.dqValidationPolicy[key].drt+" must be ").replace("_CRITERION_",profile.dqValidationPolicy[key].criterion.toLowerCase()).replace("_INDEX_",key).replace("_INDEX_",key).replace("_DESC_",profile.dqMeasurementPolicy[key].description);
//     });
//     $("#dq-validation-policy-content").html(dqValidationPolicyContent).uitooltip({
//       show: {
//         effect: "slideDown",
//         delay: 250
//       }
//     });    
// }    
// function save(){
//     if(localStorage) localStorage.profile = JSON.stringify(profile);
//     else alert("Sorry, this resource doen't work in your Internet browser.");  
// }

// if (localStorage && localStorage.profile) {                
//     profile = JSON.parse(localStorage.profile);
//     $("#i-use-case-name").val(profile.useCase.name);
//     $("#i-use-case-description").val(profile.useCase.description);    
// }
    
// updateProfile();
// updatePolicy();