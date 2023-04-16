### @RequestBody
HTTP 요청으로 넘어오는 body의 내용을 HttpMessageConverter를 통해 Java Objec로 역직렬화한다  
  
multipart 요청이 아닌, 어떤 바이너리 파일을 포함하고 있지 않은 데이터를 받는 역할을 함  
  
RequestBody는 HTTP 요청으로 같이 넘어오는 Header의 Content-Type을 보고 어떤 Converter를 사용할지 정하기에 Content-Type은 반드시 명시해야한다  
  
> Content-Type의 종류(중 일부)  
> 
>application/json : {key:value}의 형태로 전송
>applcation/x-www-form-urlencoded : key=value&key=value 형태로 전송
>multipart/form-data : 파일 업로드시 사용되며 파일을 비롯한 여러 데이터가 있음 이라는 뜻을 가진다(@RequestBody로는 받을수 없다)  
  
### @RequestPart
Content-Type이 multipart/form-data와 관련된 경우에 사용함  
  
MultipartFile이 포함되는 경우에 MultiPartResolver가 동작하여 역직렬화를 하게된다  
  
MultiPartFile이 포함되지 않는 경우는 @RequestBody와 같이 HttpMessageConverter가 동작함  
  
### @RequestParam
하나의 파라미터만 받을때 사용함, 기본적으로 파라미터가 필수적으로 들어오게 설정되어 있기에 파라미터가 들어오지 않는 경우 BadRequest가 발생하므로 파라미터가 들어올수도 들어오지 않을수도 있다면 ```required = false```를 주어야 함  
  
RequestParam도 @RequestPar와 같이 MultiPartFile을 받을 때 사용할 수 있음  
@RequestPart와 다른점은 @RequestParam의 경우 파라미터가 String이나 MultipartFile이 아닌 경우 Converter나 PropertyEditor에 의해 처리 되지만 @RequestPart는 HttpMessageConverter를 이용하여 Content-Type을 참고하여 처리한다는 점  
  
이때 하나의 요청 파라미터에만 대응한다고 해서 1개의 MultipartFile만 받을 수 있는게 아닌 ```List<MultipartFile>```의 형태로도 받을 수 있으며

모든 파라미터를 ```Map<String, String>```처럼 한 번에 받을 수 있으나 많은 데이터를 하나의 파라미터로 받는 것은 유지 보수성의 측면에서 좋지 못 하므로 많은 데이터를 주고받는 경우에는 @RequestBody와 DTO를 이용하는 편이 좋음