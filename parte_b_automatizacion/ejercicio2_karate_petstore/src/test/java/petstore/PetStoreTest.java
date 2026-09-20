package petstore;

import com.intuit.karate.junit5.Karate;

public class PetStoreTest {

    @Karate.Test
    Karate testPetStore() {
        return Karate.run("classpath:petstore/petstore.feature");
    }
}
