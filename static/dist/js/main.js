function add_image(input, block){
    if (input.files && input.files[0]){
        let reader = new FileReader();
        console.log($('#'+block).parent()[0])
        reader.onload = function (e){
            $('#'+block).attr('src', e.target.result);
            $('#label_'+block).parent().attr('class', 'form-group has-success')
        };
        reader.readAsDataURL(input.files[0]);
    }
}





function check_text(id){
    if ($('#'+id.id)[0].value !== ''){
        $('#'+id.id).parent()[0].setAttribute('class', 'form-group has-success')
    }else{
        $('#'+id.id).parent()[0].setAttribute('class', 'form-group has-error')
    }
}

function check_text_new(id){
    if ($('#'+id.id)[0].value !== ''){
        $('#'+id.id).parent()[0].classList.add('has-success')
        $('#'+id.id).parent()[0].classList.remove('has-error')
    }else{
        $('#'+id.id).parent()[0].classList.add('has-error')
        $('#'+id.id).parent()[0].classList.remove('has-success')
    }
}


function add_new_form(){
    if(event){
        event.preventDefault()
    }
    const TotalFormCount = document.getElementById('id_section-TOTAL_FORMS');
    const currentCount = parseInt(TotalFormCount.value);
    console.log(currentCount)
    const CopyTarget = document.getElementById('section-tab-pane');
    const EmptyFormEl = document.getElementById('empty-section-form').cloneNode(true);
    EmptyFormEl.setAttribute('class', 'mt-2 d-block');
    EmptyFormEl.setAttribute('id', `section-${currentCount}`);
    const regex = RegExp('__prefix__', 'g');
    EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`);
    TotalFormCount.setAttribute('value', `${currentCount + 1}`);

    CopyTarget.append(EmptyFormEl);

    console.log(document.getElementById(`id_section-${currentCount}-name_section`));
}

function add_new_service_form(){
    if(event){
        event.preventDefault()
    }
    const TotalFormCount = document.getElementById('id_service-TOTAL_FORMS');
    const currentCount = parseInt(TotalFormCount.value);
    console.log(currentCount)
    const CopyTarget = document.getElementById('form-service');
    const EmptyFormEl = document.getElementById('empty-service-form').cloneNode(true);
    EmptyFormEl.setAttribute('class', 'col-md-4');
    EmptyFormEl.setAttribute('id', `service-${currentCount}`);
    const regex = RegExp('__prefix__', 'g');
    EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`);
    TotalFormCount.setAttribute('value', `${currentCount + 1}`);

    CopyTarget.append(EmptyFormEl);

    console.log(document.getElementById(`id_section-${currentCount}-name_section`));
}

function add_new_floor_form(){
    if(event){
        event.preventDefault()
    }
    const TotalFormCount = document.getElementById('id_floor-TOTAL_FORMS');
    const currentCount = parseInt(TotalFormCount.value);
    console.log(currentCount)
    const CopyTarget = document.getElementById('floor-tab-pane');
    const EmptyFormEl = document.getElementById('empty-floor-form').cloneNode(true);
    EmptyFormEl.setAttribute('class', 'mt-2 d-block');
    EmptyFormEl.setAttribute('id', `floor-${currentCount}`);
    const regex = RegExp('__prefix__', 'g');
    EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`);
    TotalFormCount.setAttribute('value', `${currentCount + 1}`);
    console.log(document.getElementById(`id_floor-${currentCount}-name-floor`));

    CopyTarget.append(EmptyFormEl);
}

function add_new_document(){
    if(event){
        event.preventDefault()
    }
    const TotalFormCount = document.getElementById('id_document-TOTAL_FORMS');
    const currentCount = parseInt(TotalFormCount.value);
    const CopyTarget = document.getElementById('form-document-rows');
    const EmptyFormEl = document.getElementById('empty-document-form').cloneNode(true);
    EmptyFormEl.setAttribute('class', 'form-group');
    EmptyFormEl.setAttribute('id', `document-${currentCount}`);
    const regex = RegExp('__prefix__', 'g');
    EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`);
    TotalFormCount.setAttribute('value', `${currentCount + 1}`)

    CopyTarget.append(EmptyFormEl)
}

function add_new_tarrif(){
    if(event){
        event.preventDefault()
    }
    const TotalFormCount = document.getElementById('id_tarrif-TOTAL_FORMS');
    const currentCount = parseInt(TotalFormCount.value);
    const CopyTarget = document.getElementById('form-tarrif-rows');
    const EmptyFormEl = document.getElementById('empty-tarrif-form').cloneNode(true);
    EmptyFormEl.setAttribute('class', 'col-md-4');
    EmptyFormEl.setAttribute('id', `tarrif-${currentCount}`);
    const regex = RegExp('__prefix__', 'g');
    EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`);
    TotalFormCount.setAttribute('value', `${currentCount + 1}`);

    CopyTarget.append(EmptyFormEl);

}

function add_new_measure(){
    if(event){
        event.preventDefault()
    }
    const TotalFormCount = document.getElementById('id_measure-TOTAL_FORMS');
    const currentCount = parseInt(TotalFormCount.value);
    const CopyTarget = document.getElementById('form-measure-rows');
    const EmptyFormEl = document.getElementById('empty-measure-form').cloneNode(true);
    EmptyFormEl.setAttribute('class', 'row');
    EmptyFormEl.setAttribute('id', `measure-${currentCount}`);
    const regex = RegExp('__prefix__', 'g');
    EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`);
    TotalFormCount.setAttribute('value', `${currentCount + 1}`);

    CopyTarget.append(EmptyFormEl);
}

function add_new_setting(name){
    if(event){
        event.preventDefault()
    }
    const TotalFormCount = document.getElementById(`id_${name}-TOTAL_FORMS`);
    const currentCount = parseInt(TotalFormCount.value);
    const CopyTarget = document.getElementById(`form-${name}-rows`);
    const EmptyFormEl = document.getElementById(`empty-${name}-form`).cloneNode(true);
    EmptyFormEl.setAttribute('class', 'row');
    EmptyFormEl.setAttribute('id', `${name}-${currentCount}`);
    const regex = RegExp('__prefix__', 'g');
    EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`);
    TotalFormCount.setAttribute('value', `${currentCount + 1}`);

    CopyTarget.append(EmptyFormEl);
}


function delete_form(id){
    console.log(id.value)
    let button_this = id.value;
    Swal.fire({
        title: 'Ви впевнені ?',
        confirmButtonColor: '#3085d6',
        showCancelButton: true,
        cancelButtonColor: '#d33',
        confirmButtonText: 'Delete!'
    }).then((result) => {
        if (result.isConfirmed){
            Swal.fire({
              position: 'center',
              icon: 'success',
              title: 'Видалено',
              showConfirmButton: false,
              timer: 900
            })
                document.querySelector('#'+button_this).setAttribute('class', 'd-none');
                document.getElementById(`id_${button_this}-DELETE`).setAttribute('checked', '')
        }
    })
}

function hide_tarrif_form(id){
    let block_id = document.getElementById(`${id.parentElement.parentElement.id}`);
    block_id.setAttribute('class', 'd-none');
    let countForm = document.getElementById('id_tarrif-TOTAL_FORMS');
    let count = parseInt(countForm.value);
    countForm.setAttribute('value', `${count-1}`)
}

function delete_form_formset(id){
    console.log(id)
    Swal.fire({
        title: 'Ви впевнені ?',
        confirmButtonColor: '#3085d6',
        showCancelButton: true,
        cancelButtonColor: '#d33',
        confirmButtonText: 'Delete!'
    }).then((result) => {
        if (result.isConfirmed){
            Swal.fire({
              position: 'center',
              icon: 'success',
              title: 'Видалено',
              showConfirmButton: false,
            })
                document.querySelector('#'+id).setAttribute('class', 'd-none');
                document.getElementById(`id_${id}-DELETE`).setAttribute('checked', 'true')

        }
    })
}

// Строка таблицы ссылка
    $(document).on('click', '.linkedRow tbody tr', function(event) {
        // Перевірка, чи td містить елементи <a>, <svg> або <checkbox>
        var target = $(event.target);
        if (target.closest('td').find('a, svg, :checkbox').is(target)) {
            return;
        }

        var url = $(this).data('href');
        console.log('URL:', url)
        if (url) {
            document.location.href = $(this).data('href');
        }
    }).find('a, button, input, select, textarea').hover(function() {
        $(this).parents('tr').unbind('click');
    }, function() {
        $(this).parents('tr').click(function() {
            var url = $(this).data('href');
            if (url) {
                document.location.href = $(this).data('href');
            }
        });
    });
    // Строка таблицы ссылка

        // Кнопка показать пароль
    function showPassword(id){
        var inputText = $('.pass-value');
        var inputType = inputText.prop('type');
        if (inputType === 'password') {
            inputText.prop('type', 'text');
            $(id).children().removeClass('fa-eye-slash').addClass('fa-eye');
        } else {
            inputText.prop('type', 'password');
            $(id).children().removeClass('fa-eye').addClass('fa-eye-slash');
        }
    }
    // Кнопка показать пароль
function delete_service(id){
    console.log(id)
    console.log(id)
}

$(document).ready(function (){
    const TotalFormCount = document.getElementById('id_general-TOTAL_FORMS');
    const currentCount = parseInt(TotalFormCount.value);
    console.log(currentCount);
    const FileRename = document.getElementById('new_image')
    console.log(FileRename)
    const regex = RegExp('__prefix__', 'g');
    FileRename.innerHTML = FileRename.innerHTML.replace(regex, `${currentCount}`)
    document.getElementById(`id_general-${currentCount}-image`).addEventListener('change', function (){
        TotalFormCount.setAttribute('value', `${currentCount + 1}`)
    })
})


$(document).ready(function (){
    const TotalFormCount = document.getElementById('id_extra-TOTAL_FORMS');
    const currentCount = parseInt(TotalFormCount.value);
    console.log(currentCount);
    const FileRename = document.getElementById('new_extra_image')
    console.log(FileRename)
    const regex = RegExp('__prefix__', 'g');
    FileRename.innerHTML = FileRename.innerHTML.replace(regex, `${currentCount}`)
    document.getElementById(`id_extra-${currentCount}-image`).addEventListener('change', function (){
        TotalFormCount.setAttribute('value', `${currentCount + 1}`);
    })
})


$(document).ready(function (){
   const countValue = document.getElementById('id_block-TOTAL_FORMS').getAttribute('value')
    console.log(countValue)
    for(let i=0; i<countValue; i++){
        console.log(i)
      const ConstForm = document.getElementById('block-'+i);
      const regex = RegExp('__prefix__', 'g')
      ConstForm.innerHTML = ConstForm.innerHTML.replace(regex, i)
  }
 })

$(document).ready(function (){
   const countValue = document.getElementById('id_service-TOTAL_FORMS').getAttribute('value')
    console.log(countValue)
    for(let i=0; i<countValue; i++){
        console.log(i)
      const ConstForm = document.getElementById('service-'+i);
      const regex = RegExp('__prefix__', 'g')
      ConstForm.innerHTML = ConstForm.innerHTML.replace(regex, i)
  }
 })

function check_value(href_link){
       Swal.fire({
        title: 'Ви впевнені ?',
        confirmButtonColor: '#3085d6',
        showCancelButton: true,
        cancelButtonColor: '#d33',
        confirmButtonText: 'Delete!'
    }).then((result) => {
        if (result.isConfirmed){
                window.location.href = href_link
        }
    })
}

//Перевірка поля з поштою
function isEmail(email) {
        let regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        console.log(event.target.id)
        let email_input = $('#' + event.target.id)[0].parentElement;
        console.log(regex.test(email))
    if(regex.test(email) === false){
        email_input.classList.add('has-error');
        email_input.classList.remove('has-success');
        console.log()
    }else{
        email_input.classList.add('has-success');
        email_input.classList.remove('has-error');
    }
}
//**Перевірка поля з поштою**

function isSelect(select){
        console.log(select.parentElement)
        select.classList.add('has-select-success');
        select.parentElement.classList.add('has-success')
}

function add_new_receipt_service(){
                    if(event){
                        event.preventDefault()
                    }
                    const TotalFormCount = document.getElementById('id_receipt-service-TOTAL_FORMS');
                    const currentCount = parseInt(TotalFormCount.value);
                    const CopyTarget = document.getElementById('form-receipt-service-rows');
                    const EmptyFormEl = document.getElementById('empty-receipt-service-form').cloneNode(true);
                    EmptyFormEl.setAttribute('class', '');
                    EmptyFormEl.setAttribute('id', `receipt-service-${currentCount}`);
                    const regex = RegExp('__prefix__', 'g');
                    EmptyFormEl.innerHTML = EmptyFormEl.innerHTML.replace(regex, `${currentCount}`);
                    TotalFormCount.setAttribute('value', `${currentCount + 1}`);

                    CopyTarget.append(EmptyFormEl);
                }





