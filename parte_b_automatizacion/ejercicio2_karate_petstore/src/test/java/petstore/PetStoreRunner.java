package petstore;

import com.intuit.karate.junit5.Karate;

class PetStoreRunner {

    @Karate.Test
    Karate testPetStore() {
        return Karate.run("petstore").relativeTo(getClass());
    }
}
